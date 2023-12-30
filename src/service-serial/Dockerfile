FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN python check.py

RUN if [ $? -eq 0 ]; then python script.py; else echo "No PORT CONNECTED"; fi
