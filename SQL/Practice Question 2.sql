CREATE DATABASE col;
USE col;

CREATE TABLE stu(
	rollno INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT NOT NULL,
    grade VARCHAR(1),
    city VARCHAR(20)
);

INSERT INTO stu VALUES
(101,"Anil",78,"C","Pune"),
(102,"Bhumika",93,"A","Mumbai"),
(103,"Chetan",85,"B","Mumbai"),
(104,"Dhruv",96,"A","Delhi"),
(105,"emanuel",12,"F","Delhi"),
(106,"Farah",82,"B","Delhi");

SELECT name,marks FROM stu;
SELECT DISTINCT city FROM stu;

SELECT * FROM stu WHERE marks > 80;
SELECT * FROM stu WHERE city = "Mumbai";

SELECT * FROM stu WHERE marks > 80 AND city = "Delhi";
SELECT * FROM stu WHERE marks > 80 OR city = "Mumbai";
SELECT * FROM stu WHERE marks BETWEEN 80 AND 90; 

SELECT * FROM stu WHERE city IN("Gurugram","Delhi","Pune");

SELECT * FROM stu WHERE city NOT IN("Gurugram","Delhi","Pune");