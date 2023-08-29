FROM python:3

# Sets dumping log messages directly to stream instead of buffering
# ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app


COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000
