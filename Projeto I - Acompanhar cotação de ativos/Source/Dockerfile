

# Specify a Python image

FROM python:3.12

# Define some enviromental variables to improv performance in python

# This env variable don't let python to write .pyc files and saves memory
ENV PYTHONDONTWRITEBYTECODE = 1 
# This env makes sure the output goes directly to terminal
ENV PYTHONUNBUFFERED = 1


#Defines a workinf directory inside the container
WORKDIR /code/

# Create a venv to install the requirements isolated
#RUN Python -m venv /opt/venv

COPY /Code/Model/requirements.txt /code/Model/
RUN pip install --no-cache-dir -r /code/Model/requirements.txt

# Copy the entire source code to the container
COPY . /code/

# Makes the container to run indeffinitly
ENTRYPOINT [ "tail", "-f", "/dev/null" ]