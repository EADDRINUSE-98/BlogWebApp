#!/bin/bash

set -euxo pipefail

cd /home/priyanshu/Documents/Codes/Python/Django_roadmap/Project3-BlogWebApp/BlogWebApp

source .venv/bin/activate

exec gunicorn --workers 2 blog_site.wsgi
