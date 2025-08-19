SELECT * FROM student;

ALTER TABLE student
CHANGE name full_name VARCHAR(50);

DELETE FROM student WHERE marks < 80;

ALTER TABLE student
DROP COLUMN grade;
