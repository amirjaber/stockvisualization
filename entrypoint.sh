#!/usr/bin/env bash
PORT=3000
flask db upgrade
flask run --host=0.0.0.0 --port=3000
