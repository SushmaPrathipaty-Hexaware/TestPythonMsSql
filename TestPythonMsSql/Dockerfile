# For more information, please refer to https://aka.ms/vscode-docker-python
# use slim version for lower image size
FROM python:3.8-slim

# Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
# initialize working directory
WORKDIR /app
# Install & use pipenv
COPY requirements.txt /app/
RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev
RUN apt-get install -y gcc
RUN pip install -r requirements.txt
COPY . /app 
CMD ["python","main.py"]