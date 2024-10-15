FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir flask flasgger

EXPOSE 8080

CMD ["python", "app.py"]

