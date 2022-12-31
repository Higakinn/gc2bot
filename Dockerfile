FROM python:3.8-alpine

RUN pip install Mastodon.py pytube

WORKDIR /mnt
