CREATE DATABASE newStudents;

CREATE TABLE student(
	rollNo INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT NOT NULL,
    grade VARCHAR(1),
    city VARCHAR(50)
);

INSERT INTO student VALUES
(101,"Anil",78,"C","Pune"),
(102,"Bhumika",93,"A","Mumbai"),
(103,"Chetan",85,"B","Mumbai"),
(104,"Dhruv",96,"A","Delhi"),
(105,"emanuel",12,"F","Delhi"),
(106,"Farah",82,"B","Delhi");

SELECT DISTINCT city FROM student;

SELECT city,avg(marks)
FROM student
GROUP BY city
ORDER BY avg(marks) DESC;


SELECT grade,count(rollNo) FROM student GROUP BY grade ORDER BY grade;

SELECT city,count(rollNo) FROM student GROUP BY city HAVING max(marks) > 90;