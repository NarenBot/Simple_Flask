FROM python:3.8-slim-buster
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "app.py"]