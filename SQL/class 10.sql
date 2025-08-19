SELECT * FROM student;
SELECT AVG(marks)
FROM student;

SELECT name,marks
FROM student
WHERE marks > 74.3333;

SELECT name,marks
FROM student
WHERE marks > (SELECT AVG(marks) FROM student);

SELECT rollno FROM student
WHERE rollno % 2 = 0;

SELECT name,rollno FROM student
WHERE rollno IN
(102,104,106);

SELECT name,rollno
FROM student
WHERE rollno IN (SELECT rollno FROM student WHERE rollno % 2 = 0);

SELECT * FROM student
WHERE city = "Delhi";

SELECT max(marks) FROM (SELECT * FROM student WHERE city = "Delhi") as temp;
SELECT max(marks) FROM (SELECT * FROM student WHERE city = "Mumbai") as temp;

SELECT (SELECT max(marks) FROM student),name FROM student;
SELECT max(marks) FROM student WHERE city = "Mumbai";

CREATE VIEW view1 AS
SELECT rollno,name,marks FROM student;

SELECT * FROM view1
WHERE marks > 90;