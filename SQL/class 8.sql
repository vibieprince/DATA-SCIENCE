CREATE DATABASE college;

CREATE TABLE student(
	id INT PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO student (id,name)
VALUES
(101,"Alice"),
(102,"Bob"),
(103,"Casey");

CREATE TABLE course(
	id INT PRIMARY KEY,
    course VARCHAR(50)
);

INSERT INTO course(id,course)
VALUES
(102,"English"),
(105,"Math"),
(103,"Science"),
(107,"Computer Science");

SELECT * FROM student;
SELECT * FROM course;

SELECT * 
FROM student
INNER JOIN course
ON student.id = course.id;

SELECT * 
FROM student as s
INNER JOIN course as c
ON s.id = c.id;

SELECT * 
FROM student
LEFT JOIN course
ON student.id = course.id;

SELECT * 
FROM student
RIGHT JOIN course
ON student.id = course.id;

SELECT * 
FROM student
LEFT JOIN course
ON student.id = course.id
UNION
SELECT * 
FROM student
RIGHT JOIN course
ON student.id = course.id;

SELECT *
FROM student as s
LEFT JOIN course as c
ON s.id = c.id
WHERE c.id IS NULL;

SELECT *
FROM student as s
RIGHT JOIN course as c
ON s.id = c.id
WHERE s.id IS NULL;