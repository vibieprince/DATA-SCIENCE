SELECT * FROM employee;
INSERT INTO employee(
	name,
	position,
	department,
	joining_date,
	salary
) VALUES ('Prince Singh','Data Analyst','Data Science','2025-09-11',65000.00),
         ('Mrityunjay Thakhur','Senior Developer','GAIL INDIA','2019-09-12',45000.00),
		 ('Nakul Sharma','Assistant Proffessor','GL BAJAJ','16-10-2023',80000.00),
		 ('Saurabh Patel','Marketing Specialist','Marketing','2020-11-25',50000.00),
		 ('Akash Singh','Sales Executive','Sales','2023-02-12',62000.00);

ALTER TABLE employee
ALTER COLUMN department TYPE VARCHAR(40),
ALTER COLUMN position TYPE VARCHAR(30);

TRUNCATE TABLE employee;
TRUNCATE TABLE employee START IDENTITY;