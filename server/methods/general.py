from server import utils
from server import cache
import requests
import config
from functools import lru_cache  # Importing lru_cache


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
    @cache.memoize(timeout=config.cache)
    def supply(cls):
        data = utils.make_request("getblockchaininfo")
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
        @lru_cache(maxsize=128)
        def price(cls):
            link = "https://api.coinpaprika.com/v1/tickers/mwc-minersworldcoin"
            
            try:
                response = requests.get(link)
                data = response.json()

                # Return the full data structure including quotes
                return data  # This includes everything (price, volume, market cap, etc.)
            except requests.exceptions.RequestException as e:
                print(f"Error fetching price: {e}")
                return None
