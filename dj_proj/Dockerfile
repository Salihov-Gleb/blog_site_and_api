FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYCODE=1
WORKDIR /dj_proj/

RUN apk --update add \
    build-base \
    jpeg-dev \
    zlib-dev

RUN pip install --upgrade pip
COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r ./requirements.txt
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT [ "dj_proj/entrypoint.sh" ]