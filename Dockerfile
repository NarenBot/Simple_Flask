FROM python:3.8
COPY . /app
WORKDIR /app
# RUN pip install --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --upgrade --proxy=127.0.0.1:3128 -r requirements.txt
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
