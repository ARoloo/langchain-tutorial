FROM python:3.11-slim

WORKDIR /app

COPY python/requirements.txt python/requirements.txt

RUN pip3 install --no-cache-dir -r python/requirements.txt

copy . .

CMD ["tail", "-f", "/dev/null"]
