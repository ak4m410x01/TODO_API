# pull official base image
FROM python:3.11

# author name
LABEL author="ak4m410x01"

# set work directory
WORKDIR /app

# set default shell
SHELL [ "/bin/bash", "-c" ]

# update/upgrade container & install git
RUN apt update -qqq && \
    apt upgrade -y -qqq && \
    apt install -y git

# clone repo into
RUN git clone https://github.com/ak4m410x01/TODO_API/ .
RUN rm -rf .git/ README.md api.Dockerfile docker-compose.yml

# copy .env files [containers SECRET VARIABLES] LIKE database username and password
COPY .env .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install required packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# expose port
EXPOSE 80