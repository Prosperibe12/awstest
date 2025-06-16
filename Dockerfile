FROM python:3.12-slim-bullseye

RUN apt-get update && \ 
  apt-get upgrade -y && \ 
  apt-get clean && \ 
  rm -rf /var/lib/apt/lists/* && \
  python -m pip install --upgrade pip

WORKDIR /app 

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt 

COPY . /app

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]