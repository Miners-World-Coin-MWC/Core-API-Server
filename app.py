from server import config
# from server import sio
from server import app

if __name__ == "__main__":
    app.run(host=config.host, port=config.port, debug=config.debug)
