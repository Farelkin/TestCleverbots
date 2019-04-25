FROM python:3.5.2

COPY ./cleverbots /home/cleverbots
WORKDIR /home/cleverbots

RUN pip install -r requirements.txt
RUN pip install --upgrade pip
RUN python manage.py migrate