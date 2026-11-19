from flask import Response, Blueprint, jsonify, request
from server.methods.transaction import Transaction
from server.methods.general import General
from server.methods.address import Address
from webargs.flaskparser import use_args
from server.methods.block import Block
from webargs import fields
from server import stats
from server import utils
from functools import lru_cache
import re
import ipaddress

blueprint = Blueprint("rest", __name__)

offset_args = {"offset": fields.Int(missing=0)}

amount_args = {"amount": fields.Int(missing=0)}


@stats.rest
@blueprint.route("/info", methods=["GET"])
def get_info():
    return jsonify(General().info())


@stats.rest
@blueprint.route("/height/<int:height>", methods=["GET"])
@use_args(offset_args, location="query")
def block_by_height(args, height):
    offset = args["offset"]

    data = Block().height(height)
    if data["error"] is None:
        data["result"]["tx"] = data["result"]["tx"][offset : offset + 10]

    return jsonify(data)


@stats.rest
@blueprint.route("/hash/<int:height>", methods=["GET"])
def hash_by_height(height):
    return jsonify(Block().get(height))


@stats.rest
@blueprint.route("/range/<int:height>", methods=["GET"])
@use_args(offset_args, location="query")
def blocks_by_range(args, height):
    offset = args["offset"]

    if offset > 100:
        offset = 100

    result = Block().range(height, offset)
    return jsonify(utils.response(result))


@stats.rest
@blueprint.route("/block/<string:bhash>", methods=["GET"])
@use_args(offset_args, location="query")
def block_by_hash(args, bhash):
    offset = args["offset"]

    data = Block().hash(bhash)
    if data["error"] is None:
        data["result"]["tx"] = data["result"]["tx"][offset : offset + 10]

    return jsonify(data)


@stats.rest
@blueprint.route("/header/<string:bhash>", methods=["GET"])
def block_header(bhash):
    data = utils.make_request("getblockheader", [bhash])
    if data["error"] is None:
        data["result"]["txcount"] = data["result"]["nTx"]
        data["result"].pop("nTx")

    return jsonify(data)


@stats.rest
@blueprint.route("/transaction/<string:thash>", methods=["GET"])
def transaction_info(thash):
    return jsonify(Transaction().info(thash))


@stats.rest
@blueprint.route("/balance/<string:address>", methods=["GET"])
def address_balance(address):
    return jsonify(Address().balance(address))


@stats.rest
@blueprint.route("/history/<string:address>", methods=["GET"])
@use_args(offset_args, location="query")
def address_history(args, address):
    offset = args["offset"]

    data = Address().history(address)
    if data["error"] is None:
        data["result"]["tx"] = data["result"]["tx"][offset : offset + 10]

    return jsonify(data)


@stats.rest
@blueprint.route("/mempool/<string:address>", methods=["GET"])
def address_mempool(address):
    return jsonify(Address().mempool(address))


@stats.rest
@blueprint.route("/unspent/<string:address>", methods=["GET"])
@use_args(amount_args, location="query")
def address_unspent(args, address):
    amount = args["amount"]
    return jsonify(Address().unspent(address, amount))


@stats.rest
@blueprint.route("/mempool", methods=["GET"])
def mempool_info():
    return jsonify(General().mempool())


@stats.rest
@blueprint.route("/decode/<string:raw>", methods=["GET"])
def decode_raw_tx(raw):
    return jsonify(Transaction().decode(raw))


@stats.rest
@blueprint.route("/fee", methods=["GET"])
def estimate_fee():
    return jsonify(General().fee())


@stats.rest
@blueprint.route("/broadcast", methods=["POST"])
def broadcast():
    raw = request.values.get("raw")
    return Transaction().broadcast(raw)


@stats.rest
@blueprint.route("/supply", methods=["GET"])
def supply():
    data = General().supply()
    return jsonify(utils.response(data))


@stats.rest
@blueprint.route("/supply/plain", methods=["GET"])
def supply_plain():
    data = int(utils.amount(General().supply()["supply"]))
    return Response(str(data), mimetype="text/plain")


##ts.ret
#@blueprint.route("/faucet/drain", methods=["POST"])
#def faucet_drain():
#    ip = request.headers.get('X-Real-IP', request.remote_addr)
#    address = request.json.get("address")
#    data = Faucet().drain(address, ip)
#    return jsonify(data)
#
#@stats.rest
#@blueprint.route("/faucet/balance", methods=["GET"])
#def faucet_balance():
#    data = Faucet().balance()
#    return jsonify(data)

@stats.rest
@blueprint.route('/price', methods=['GET'])
def price():
    data = General.CoinData.price()  # Fetch the full data
    if data:
        return jsonify(data)  # Return the full data as JSON response
    else:
        return jsonify({"error": "Unable to fetch price data"}), 500

@stats.rest
@blueprint.route("/peers", methods=["GET"])
def peers():
    peer_data = utils.make_request("getpeerinfo")

    if peer_data["error"] is not None:
        return jsonify(peer_data)

    peers = peer_data["result"]
    enriched_peers = []

    for peer in peers:
        raw_addr = peer.get("addr", "")
        ip = extract_ip(raw_addr)

        enriched_peers.append({
            "addr": ip,
            "subver": peer.get("subver", "N/A"),
            "pingtime": peer.get("pingtime", 0),
            # "country": "Unknown"  # Placeholder for country as you're handling it in HTML
        })

    return jsonify({"result": enriched_peers, "error": None})


def extract_ip(addr):
    if not addr:
        return "Unknown"
    if addr.startswith('['):  # IPv6
        match = re.match(r'\[(.*?)\]', addr)
        return match.group(1) if match else "Unknown"
    return addr.rsplit(":", 1)[0]



def init(app):
    app.register_blueprint(blueprint, url_prefix="/")
