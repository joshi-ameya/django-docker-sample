FROM python:3
# ENV PYTHONUNBUFFERED 1
# RUN apt-get update && apt-get -y install postgresql
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY /requirements /code/
RUN pip install -r requirements.txt
COPY src /code
# RUN python src/manage.py migrate