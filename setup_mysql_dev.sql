-- a script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_deb
CREATE USER

IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd'
GRANT ALL PRIVILEGES
ON 'hbnb_dev_db'.*
TO 'hbnb_dev'@'localhost'
IDENTIFEID BY 'hbnb_dev_pwd'
GRANT SELECT
ON 'hbnb_dev_db'.*
TO 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnh_dev_db_pwd'
FLUSH PRIVILEGES
