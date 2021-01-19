FROM python:3
ENV PYTHONUNBUFFERED 1

# EXPOSE 5432

RUN mkdir /code
WORKDIR /code
RUN mkdir /code/static
COPY requirements.txt /code/
COPY requirements /code/requirements
RUN pip install -r requirements.txt
COPY . /code/