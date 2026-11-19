from server import utils
from server import cache
import requests
import config


class General:
    @classmethod
    def info(cls):
        data = utils.make_request("getblockchaininfo")

        if data["error"] is None:
            data["result"]["supply"] = utils.supply(data["result"]["blocks"])[
                "supply"
            ]
            data["result"]["reward"] = utils.reward(data["result"]["blocks"])

            if "verificationprogress" in data["result"]:
                data["result"].pop("verificationprogress")
            if "initialblockdownload" in data["result"]:
                data["result"].pop("initialblockdownload")
            if "pruned" in data["result"]:
                data["result"].pop("pruned")
            if "softforks" in data["result"]:
                data["result"].pop("softforks")
            if "bip9_softforks" in data["result"]:
                data["result"].pop("bip9_softforks")
            if "warnings" in data["result"]:
                data["result"].pop("warnings")
            if "size_on_disk" in data["result"]:
                data["result"].pop("size_on_disk")

            nethash = utils.make_request(
                "getnetworkhashps", [120, data["result"]["blocks"]]
            )
            if nethash["error"] is None:
                data["result"]["nethash"] = int(nethash["result"])

        return data

    @classmethod
    def supply(cls):
        data = utils.make_request("getblockchaininfo")
        if data["error"] is not None:
            return data
        height = data["result"]["blocks"]
        result = utils.supply(height)
        result["height"] = height

        return result

    @classmethod
    def fee(cls):
        # ToDo: Fix me
        # https://github.com/sugarchain-project/sugarchain/issues/34

        # data = utils.make_request("estimatesmartfee", [6])

        # if data["error"] is None:
        #   data["result"]["feerate"] = utils.satoshis(data["result"]["feerate"])

        # return data

        return utils.response({"feerate": utils.satoshis(0.01), "blocks": 30})

    @classmethod
    @cache.memoize(timeout=60)
    def fee_estimates(cls):
        targets = (1, 2, 3, 6, 12, 24)
        estimates = {}
        errors = {}

        for target in targets:
            data = utils.make_request("estimatesmartfee", [target])
            if data.get("error") is not None:
                errors[str(target)] = data["error"].get("message", "Estimate unavailable")
                continue

            result = data.get("result") or {}
            fee_rate = result.get("feerate")
            if fee_rate is None:
                errors[str(target)] = "Insufficient node data for this confirmation target"
                continue

            # estimatesmartfee reports MWC per kilobyte; expose satoshis per virtual byte.
            try:
                fee_rate = float(fee_rate)
            except (TypeError, ValueError):
                errors[str(target)] = "Node returned an invalid fee estimate"
                continue
            if fee_rate <= 0:
                errors[str(target)] = "Insufficient node data for this confirmation target"
                continue
            estimates[str(target)] = round(fee_rate * 100000, 3)

        if not estimates:
            return utils.error_response(
                "The node could not provide a fee estimate",
                503,
                details={"targets": errors},
            )

        return utils.response(
            {
                "estimates": estimates,
                "unit": "sat/vB",
                "source": "estimatesmartfee",
                "unavailable_targets": errors,
            }
        )

    @classmethod
    def mempool(cls):
        data = utils.make_request("getmempoolinfo")

        if data["error"] is None:
            if data["result"]["size"] > 0:
                mempool = utils.make_request("getrawmempool")["result"]
                data["result"]["tx"] = mempool
            else:
                data["result"]["tx"] = []

        return data

    class CoinData:
        @classmethod
        @cache.memoize(timeout=300)
        def price(cls):
            link = "https://api.coinpaprika.com/v1/tickers/mwc-minersworldcoin"
            
            try:
                response = requests.get(link, timeout=getattr(config, "http_timeout", 10))
                response.raise_for_status()
                data = response.json()

                # Return the full data structure including quotes
                return data  # This includes everything (price, volume, market cap, etc.)
            except (requests.exceptions.RequestException, ValueError) as e:
                print(f"Error fetching price: {e}")
                return None
