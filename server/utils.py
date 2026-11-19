import requests
import config
import math
import json


def dead_response(message="Invalid Request", rid=config.rid):
    return {"error": {"code": 404, "message": message}, "id": rid}


def error_response(message, code=502, rid=config.rid, details=None):
    error = {"code": code, "message": message}
    if details is not None:
        error["details"] = details
    return {"error": error, "id": rid, "result": None}


def response(result, error=None, rid=config.rid):
    return {"error": error, "id": rid, "result": result}


def make_request(method, params=[]):
    headers = {"content-type": "text/plain;"}
    data = json.dumps({"id": config.rid, "method": method, "params": params})

    try:
        result = requests.post(
            config.endpoint,
            headers=headers,
            data=data,
            timeout=getattr(config, "rpc_timeout", 10),
        ).json()
        return result
    except requests.exceptions.Timeout:
        return error_response("Blockchain node request timed out", 504)
    except requests.exceptions.ConnectionError:
        return error_response("Unable to connect to the blockchain node", 503)
    except (requests.exceptions.RequestException, ValueError):
        return error_response("Invalid response from the blockchain node", 502)


def reward(height):
    halvings = height // 300000

    if halvings >= 64:
        return 0

    return int(satoshis(300 - (300 * 0.1)) // (2**halvings))


def supply(height):
    reward = satoshis(300 - (300 * 0.1))
    halvings = 300000
    halvings_count = 0
    supply = reward

    while height > halvings:
        total = halvings * reward
        reward = reward / 2
        height = height - halvings
        halvings_count += 1

        supply += total

    supply = supply + height * reward

    return {"halvings": int(halvings_count), "supply": int(supply)}


def satoshis(value):
    return math.ceil(value * math.pow(10, 8))


def amount(value):
    return round(value / math.pow(10, 8), 8)
