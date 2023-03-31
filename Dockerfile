FROM python:3.8-slim-buster
WORKDIR /src
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE $PORT
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app