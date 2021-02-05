FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y python python-pip
RUN pip3 install --cache-dir=/cache -r requirements.txt

COPY . .

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN chmod 777 src/main.py

ENTRYPOINT PYTHONPATH=. python3 src/main.py