DROP TABLE IF EXISTS students_2025;
CREATE TABLE student_2025(
	student_id INT PRIMARY KEY,
	student_name VARCHAR(100),
	course VARCHAR(50)
);

INSERT INTO student_2025 (student_id,student_name,course) VALUES
(1,'Aarav Sharma','Computer Science'),
(2,'Ishita Sharma','Mechanical Engineering'),
(3,'Kabir Patel','Electronics'),
(4,'Ananya Desai','Civil Enginerring'),
(5,'Rahul Gupta','Computer Science');

SELECT * FROM student_2025;

DROP TABLE IF EXISTS student_2026;
CREATE TABLE student_2026(
	student_id INT PRIMARY KEY,
	student_name VARCHAR(100),
	course VARCHAR(50)
);

INSERT INTO student_2026 (student_id,student_name,course) VALUES
(6,'Meera Rao','Computer Science'),
(7,'Vikram Singh','Mathematics'),
(3,'Kabir Patel','Electronics'),
(4,'Ananya Desai','Civil Enginerring'),
(8,'Sanya Kapoor','Physics');

SELECT * FROM student_2026;

-- UNION combines results, remove duplicates

SELECT student_name,course
FROM student_2025 UNION 
SELECT student_name,course
FROM student_2026;

-- UNION ALL - Combines results, keep duplicates
SELECT student_name,course
FROM student_2025 UNION ALL
SELECT student_name,course
FROM student_2026;

-- INTERSECT - Returns common results in both tables
SELECT student_name,course
FROM student_2025
INTERSECT 
SELECT student_name,course
FROM student_2026;

-- EXCEPT - Returns results in the first table but not in the second table
SELECT student_name,course
FROM student_2025
EXCEPT 
SELECT student_name,course

FROM student_2026;