FROM python:3.7.1

COPY ./cleverbots /home/cleverbots
WORKDIR /home/cleverbots

RUN pip install -r requirements.txt
RUN pip install psycopg2-binary
RUN python manage.py migrate