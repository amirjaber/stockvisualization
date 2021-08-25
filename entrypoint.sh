#!/usr/bin/env bash
echo "Use Heroku assigned port:" $PORT
flask db upgrade
flask run --host=0.0.0.0 --port=$PORT