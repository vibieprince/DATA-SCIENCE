CREATE DATABASE college;

USE college;  

CREATE TABLE student(
	id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT NOT NULL
);

INSERT INTO student VALUES(1,"PRINCE",20);
INSERT INTO student VALUES(2,"AMAN",21);

SELECT * FROM student;
DROP TABLE student;