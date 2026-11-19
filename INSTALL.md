# Installation guide

Api Server is a legacy piece of software and requires some work to be setup. This guide assumes that you already have a node of SugarChain up and running, as well as that you are using Ubuntu.

## Installing Python 3.8 (optional)

Due to the fact that Api Server uses bunch of deprecated dependencies you would need to have Python 3.8 to get it up and running. If you already have it just skip to the next section. If you don't I recommend building it from source code instead of installing from repositores as this way more reliable.

First install dependencies:

```
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev -y
```

Then get and unarchive source code for Python 3.8:

```
wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
tar -xvf Python-3.8.0.tgz
cd Python-3.8.0/
```

And build it:

```
./configure --enable-optimizations
make
sudo make altinstall
```

This way you can confirm that Python3.8

```
python3.8 --version
```

## Installing Api Server

Start by cloning this repository:

```
git clone https://github.com/sugarchain-project/api-server.git
```

Then go inside and create virtual environment:

```
cd api-server/
python3.8 -m venv venv
source venv/bin/activate
```

And install dependencies:

```
pip3 install -r requirements.txt
pip3 install webargs
```

Last step is to create `config.py` file (make sure to change SugarChain node credentials in `endpoint`):

```
rid = 'sugar-api'
cache = 3600
secret = 'SECRET'
endpoint = 'http://user:password@127.0.0.1:34229/'
host = '0.0.0.0'
port = 1234
debug = False
block_page = 10
tx_page = 25
```

## Creating Systemd service

To make Api Server run in background I suggest creating Systemd service:

```
sudo nano /etc/systemd/system/sugar-api.service
```

With this config (make sure to replace `root` with your user and change `/root/api-server` to actual path):

```
[Unit]
Description=Gunicorn instance to serve sugar api
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/root/api-server
Environment="PATH=/root/api-server/venv/bin"
ExecStart=/root/api-server/venv/bin/gunicorn app:app --worker-class eventlet -w 1 --bind 0.0.0.0:5000

[Install]
WantedBy=multi-user.target
```

Now start it:

```
sudo systemctl enable sugar-api.service
sudo systemctl start sugar-api.service
```

You can check whether Api Server is running by doing curl:

```
curl http://127.0.0.1:5000/info
```
