FROM python:3.9-alpine

WORKDIR /opt/

ARG ENVIRONMENT=dev

ENV ENVIRONMENT=${ENVIRONMENT}
ENV DJANGO_SETTINGS_MODULE=ro_help.settings.${ENVIRONMENT}

RUN pip3 install --upgrade pip setuptools \
    && wget -qO- https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-amd64-v0.2.0.tar.gz | tar -zxf - -C /usr/bin \
    && chown root:root /usr/bin/dockerize

COPY ./requirements* /opt/

RUN apk update && apk add --no-cache \
    # for Pillow
    jpeg-dev \
    zlib-dev \
    # for psycopg2
    libpq

RUN apk add --no-cache --virtual .build-deps \
    git \
    build-base \
    musl-dev \
    # these 2 are for postgres & gis
    python3-dev \
    postgresql-dev\
    # these 4 are necessary for gevent
    make \
    libffi-dev \
    file \
    && pip install --no-cache-dir -r requirements-${ENVIRONMENT}.txt \
    && apk del .build-deps

WORKDIR /opt/ro_help/

COPY ./docker/web/docker-entrypoint /
COPY ./ /opt/

ENTRYPOINT ["/docker-entrypoint"]
EXPOSE 8000
