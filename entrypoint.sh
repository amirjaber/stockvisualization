#!/usr/bin/env bash
flask db upgrade
echo "port is " $PORT
flask run --host=0.0.0.0
