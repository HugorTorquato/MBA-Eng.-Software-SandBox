

# Specify a Python image

FROM python:3.12

# Define some enviromental variables to improv performance in python

# This env variable don't let python to write .pyc files and saves memory
ENV PYTHONDONTWRITEBYTECODE = 1 
# This env makes sure the output goes directly to terminal
ENV PYTHONUNBUFFERED = 1

# Makes the container to run indeffinitly
ENTRYPOINT [ "tail", "-f", "/dev/null" ]