FROM python:3.9-slim-buster
COPY ./api_service /app
WORKDIR /app
RUN apt-get update && \
    apt-get install -y g++ curl && \
    rm -rf /var/lib/apt/lists/* && \
    pip install -r requirements.txt
CMD ["python","main.py"]