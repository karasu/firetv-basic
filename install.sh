#!/bin/bash

sudo apt-get install adb

sudo apt-get install python3-flask gunicorn3

install firetv-rest-server.py /usr/local/bin/firetv-rest-server.py

echo "To run the REST server:"
echo "cd /usr/local/bin"
echo "gunicorn -w 4 -b 127.0.0.1:4000 firetv_rest_server:app &"

