FROM library/postgres

COPY init.sql /docker-entrypoint-initdb.d/

#RUN --name demo -v "$PWD"/:/opt/demo/ -e POSTGRES_PASSWORD=password1 -d postgres
#RUN exec -it demo psql -U postgres -c "CREATE DATABASE demo_db2"
#RUN --name cleverbots -e POSTGRES_PASSWORD=cleverbots123 -d postgres
#RUN exec -it cleverbots psql -U bots -f /home/cleverbots/postgresql/init.sql