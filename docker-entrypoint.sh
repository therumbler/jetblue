#!/bin/bash
echo "starting..."

exec pipenv run gunicorn --bind=0.0.0.0 -w 4 main:app
