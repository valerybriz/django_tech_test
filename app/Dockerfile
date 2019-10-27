# Official python image
FROM python:3.7-alpine
# Enable logging in docker
ENV PYTHONUNBUFFERED 1
# Don't create pyc files on module import
ENV PYTHONDONTWRITEBYTECODE 1
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# copy/paste and install our dependencies
COPY Pipfile* /tmp/
RUN cd /tmp/ && pip install pipenv && pipenv install --system
# create directory for the app user
RUN mkdir -p /home/app
# create the app user
RUN addgroup -S app && adduser -S app -G app
# Set working dir
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app