#!/usr/bin/env bash
PORT=80
flask db upgrade
flask run --host=0.0.0.0 --port=$PORT
