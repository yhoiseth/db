#!/bin/bash
python manage.py collectstatic --noinput
python manage.py compress --force
python manage.py migrate
