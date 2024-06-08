# Specify a Python image

FROM python:3.12


RUN pip install django djangorestframework markdown django-filter

# Define some enviromental variables to improv performance in python

# This env variable don't let python to write .pyc files and saves memory
ENV PYTHONDONTWRITEBYTECODE = 1 
# This env makes sure the output goes directly to terminal
ENV PYTHONUNBUFFERED = 1

#WORKDIR /srcc
#RUN django-admin startproject escola && cd escola && django-admin startapp cursos

# Makes the container to run indeffinitly
#ENTRYPOINT ["python", "../escola/manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT [ "tail", "-f", "/dev/null" ]




## Run manually inside the container but can be here i think....

# django-admin startproject escola && cd escola
# django-admin startapp cursos