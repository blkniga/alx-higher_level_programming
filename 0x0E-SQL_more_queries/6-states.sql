-- A script that creates the database htbn_0d_usa and the table states

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE IF NOT EXISTS TABLE states(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256));
