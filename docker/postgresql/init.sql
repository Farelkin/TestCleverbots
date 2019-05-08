CREATE DATABASE cleverbots;
CREATE USER bots with NOSUPERUSER PASSWORD 'cleverbots123';
GRANT ALL PRIVILEGES ON DATABASE cleverbots TO bots;

ALTER ROLE bots SET CLIENT_ENCODING TO 'UTF8';
ALTER ROLE bots SET default_transaction_isolation TO 'READ COMMITTED';
ALTER ROLE bots SET TIME ZONE 'Europe/Moscow';