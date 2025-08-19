CREATE TABLE dept(
	id INT PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO dept VALUES (101,"English"),(102,"IT");

SELECT * FROM dept;

UPDATE dept SET id = 103 WHERE id = 102;
CREATE TABLE teacher(
	id INT PRIMARY KEY,
    name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES dept(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

INSERT INTO teacher VALUES
(101,"Adam",101),
(102,"Eve",102);

SELECT * FROM teacher;

ALTER TABLE student ADD COLUMN age INT;
SELECT * FROM student;

ALTER TABLE student
DROP COLUMN age;

ALTER TABLE student
ADD COLUMN age INT NOT NULL DEFAULT 19;

ALTER TABLE student
MODIFY COLUMN age VARCHAR(2);

ALTER TABLE student
CHANGE age stu_age INT;

INSERT INTO student (rollno,name,marks,stu_age)
VALUES
(107,"Gargi",68,100);