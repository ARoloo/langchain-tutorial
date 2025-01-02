FROM python:3.11-slim

WORKDIR /app

COPY python .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["tail", "-f", "/dev/null"]
