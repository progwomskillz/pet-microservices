FROM python:3.11.1-alpine3.17

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip --no-cache-dir

COPY . .
RUN pip install -r requirements.txt --no-cache-dir
RUN rm -rf deps/

ENTRYPOINT sh -c "while sleep 3600; do :; done"
