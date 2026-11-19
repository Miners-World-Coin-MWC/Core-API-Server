from flask import jsonify, render_template, request, send_from_directory
from server import stats
from server import utils
import config
import os


def init(app):
    @app.route("/stats")
    def app_stats():
        return jsonify(stats.info())

    @app.route("/")
    def frontend():
        return render_template("index.html")

    @app.route("/docs")
    def documentation():
        return render_template("docs.html")

    @app.route("/openapi.yaml")
    def openapi_spec():
        return send_from_directory(
            os.path.dirname(__file__), "openapi.yaml", mimetype="application/yaml"
        )

#    @app.route("/faucet", strict_slashes=False)
#    def faucet():
#        return render_template("faucet.html")    

   # @app.route("/explorer")
    #def explorer():
#	return render_template("explorer/index.html")

    @app.errorhandler(404)
    def page_404(error):
        return jsonify(utils.dead_response("Method not found")), 404


def register_versioned_aliases(app):
    """Expose the existing REST handlers beneath /api/v1 without removing old paths."""
    aliases = []
    for index, rule in enumerate(list(app.url_map.iter_rules())):
        if not rule.endpoint.startswith(("rest.", "esplora.")) and rule.endpoint != "app_stats":
            continue
        if rule.rule.startswith("/api/v1/"):
            continue

        endpoint = "api_v1_{}_{}".format(rule.endpoint.replace(".", "_"), index)
        methods = set(rule.methods or ()) - {"HEAD", "OPTIONS"}
        app.add_url_rule(
            "/api/v1" + rule.rule,
            endpoint,
            app.view_functions[rule.endpoint],
            defaults=rule.defaults,
            methods=methods,
            strict_slashes=rule.strict_slashes,
        )
        aliases.append("/api/v1" + rule.rule)

    @app.after_request
    def normalize_versioned_json(response):
        if not request.path.startswith("/api/v1/") or not response.is_json:
            return response
        if request.path.startswith("/api/v1/esplora/"):
            return response

        payload = response.get_json(silent=True)
        if not isinstance(payload, dict):
            return response

        if payload.get("error") is not None:
            error = payload["error"]
            if isinstance(error, dict):
                message = error.get("message", "Request failed")
                rpc_code = error.get("code")
                details = error.get("details")
            else:
                message = str(error)
                rpc_code = None
                details = None

            if isinstance(rpc_code, int) and 400 <= rpc_code <= 599:
                status_code = rpc_code
            elif rpc_code == -5:
                status_code = 404
            elif rpc_code in (-9, -28):
                status_code = 503
            elif rpc_code in (-8, -22):
                status_code = 400
            elif rpc_code in (-25, -26):
                status_code = 422
            elif response.status_code >= 500:
                status_code = response.status_code
            else:
                status_code = 502

            normalized_error = {"code": status_code, "message": message}
            if details is not None:
                normalized_error["details"] = details
            return jsonify({
                "error": normalized_error,
                "id": payload.get("id", config.rid),
                "result": None,
            }), status_code

        if "error" in payload and "result" in payload:
            payload.setdefault("id", config.rid)
            return jsonify(payload), response.status_code

        return jsonify({"error": None, "id": config.rid, "result": payload}), response.status_code

    return aliases
