# pull official base image
FROM python:3.7

# set work directory
WORKDIR /usr/src/app
USER root
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install djangorestframework_simplejwt
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN chmod +x /usr/src/app/start_dev.sh