FROM postgres:11-alpine

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
COPY /requirements /usr/src/app

RUN apk add --no-cache --virtual .build-deps \
  ca-certificates libressl-dev gcc python3 python3-dev py-pip linux-headers libffi-dev \
  musl-dev  jpeg-dev zlib-dev

RUN pip install -r requirements.txt

COPY src /usr/src/app