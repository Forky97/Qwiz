FROM python:3.9-alpine3.16



COPY qwizmain /qwizmain
COPY requirements.txt /temp/requirements.txt
WORKDIR /qwizmain

RUN pip install -r  /temp/requirements.txt


EXPOSE 8000
