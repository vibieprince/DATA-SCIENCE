CREATE DATABASE IF NOT EXISTS college;
DROP DATABASE IF EXISTS company;

SHOW DATABASES;
SHOW tables;
DROP DATABASE college;
CREATE TABLE student(
	rollno INT PRIMARY KEY,
    name VARCHAR(50)
);

SELECT * FROM student;

INSERT INTO student (rollno,name) VALUES (103,"Ram"),(104,"Shyam");
