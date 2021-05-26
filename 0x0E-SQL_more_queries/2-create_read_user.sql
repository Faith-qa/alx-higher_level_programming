-- create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user if it does not exist s
CREATE USER IF NOT EXISTS 'user_0d_2' IDENTIFIED BY 'user_0d_2_pwd';

-- grant SELECT previlages to user 2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;