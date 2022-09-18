# ==================
# BUILDER IMAGE
# ==================

FROM python:3.8.12-buster as builder

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/app

COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends\
    git \
    nano \
    gcc \
    unixodbc-dev \
    unixodbc \
    python3-dev \
    mariadb-client
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]