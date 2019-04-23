FROM python:3.5.2

COPY ./cleverbots /home/cleverbots
WORKDIR /home/cleverbots

RUN pip3 install -r req.txt