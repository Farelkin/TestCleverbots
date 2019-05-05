FROM nginx:latest

ADD cleverbots.conf /etc/nginx/cleverbots.conf

WORKDIR /home/cleverbots/static
RUN sudo chown -R root:root /home/cleverbots/static

WORKDIR /home/cleverbots/media
RUN sudo chown -R root:root /home/cleverbots/media