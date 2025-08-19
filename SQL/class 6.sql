SELECT * FROM student;

SET  SQL_SAFE_UPDATES = 0;

UPDATE student
SET grade = "O"
WHERE grade = "A";

UPDATE student SET marks = 82 WHERE rollno = 105;
SELECT * FROM student;

UPDATE student SET grade = "B" WHERE marks BETWEEN 80 AND 90;
SELECT * FROM student;

UPDATE student SET marks = marks+1;

SELECT * FROM student;

DELETE FROM student where marks < 33;