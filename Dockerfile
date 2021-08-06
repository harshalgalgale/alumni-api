FROM python:3.8-slim-buster

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv

ENV APP_HOME /app
ENV PORT 8080
ENV PYTHONUNBUFFERED 1

WORKDIR $APP_HOME
COPY . .

#RUN pip install --no-cache-dir -r requirements.txt
RUN pipenv install --system --deploy

CMD gunicorn --bind :$PORT --workers 1 --threads 8 alumni.wsgi:application
