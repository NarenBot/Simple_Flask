FROM ubuntu:18.04
MAINTAINER narenmohan88@gmail.com
WORKDIR /src
COPY . .
RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install gunicorn3 -y
RUN pip3 install -r requirements.txt
CMD ["gunicorn3", "-b", "0.0.0.0:8000", "app:app", "--workers=4"]