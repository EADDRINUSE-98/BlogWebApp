# Base image
FROM python:3.14-slim

# Make and set currect working directory
WORKDIR /app

# avoid making pyc files on disk
ENV PYTHONDONTWRITEBYTECODE=1
# avoid buffering stdout and stdin
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--workers", "7", "--worker-class", "gevent", "--worker-connections", "80", "--bind", "0.0.0.0:8000", "blog_site.wsgi"]
