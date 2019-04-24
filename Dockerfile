FROM python:3

COPY ./cleverbots /home/cleverbots
WORKDIR /home/cleverbots

RUN pip3 install -r req.txt