FROM python:3.11.2-alpine3.17

RUN mkdir /app
WORKDIR /app

EXPOSE 8000

RUN pip install --upgrade pip --no-cache-dir

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install -r requirements.wheels.txt
RUN rm -rf deps/

ENTRYPOINT uvicorn application.main:application --host 0.0.0.0
