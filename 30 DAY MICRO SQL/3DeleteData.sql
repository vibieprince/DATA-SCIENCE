CREATE TABLE employee2(
	employeeID INT PRIMARY KEY,
	name VARCHAR(20)NOT NULL,
	position VARCHAR(30),
	department VARCHAR(30),
	joining_date DATE,
	salary NUMERIC(10,2)
);

INSERT INTO employee2(
	employeeID,
	name,
	position,
	department,
	joining_date,
	salary
) VALUES (101,'Prince Singh','Data Analyst','Data Science','2025-09-11',65000.00),
         (402,'Mrityunjay Thakhur','Senior Developer','GAIL INDIA','2019-09-12',45000.00),
		 (141,'Nakul Sharma','Assistant Proffessor','GL BAJAJ','16-10-2023',80000.00),
		 (482,'Saurabh Patel','Marketing Specialist','Marketing','2020-11-25',50000.00),
		 (139,'Akash Singh','Sales Executive','Sales','2023-02-12',62000.00);

SELECT * FROM IF EXISTS employee2;

DELETE FROM employee2
WHERE employeeID = 482;

ALTER TABLE employee2
DROP COLUMN salary;

DROP TABLE IF EXISTS employee2;

