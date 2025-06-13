FROM python:3.12-bullseye

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=Europe/Moscow

RUN groupadd -r web && useradd -r -g web web

RUN apt update && \
    apt install -y netcat-openbsd tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./entrypoint.sh /web/entrypoint.sh

COPY ./ .

RUN chown -R web:web /code && \
    chown -R web:web /web

RUN chmod +x /web/entrypoint.sh