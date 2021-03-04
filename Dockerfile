FROM python:3.8-slim

WORKDIR /app
RUN apt-get -y update
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY helloworld.py .
CMD ["python", "helloworld.py"]
