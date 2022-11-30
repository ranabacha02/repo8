{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Using an alpine-linux base image with python installed in it\
FROM python:3.11-alpine\
# changing directory to an empty directory, /app/ (created automatically)\
# copying all the files from the BlankDjango (host file system) to /app/ (container file system)\
# note that this command will take .dockerignore into consideration\
COPY . .\
# Downloading the needed dependencies\
RUN pip install -r requirements.txt\
# Setting up the DB\
RUN python manage.py makemigrations\
RUN python manage.py migrate\
# Opening port 8000 in container\
EXPOSE 8000/tcp\
# command to be executed when container is running\
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]\
}