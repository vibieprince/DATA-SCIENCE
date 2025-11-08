CREATE TABLE Employees(
	employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	department_id INT
);

INSERT INTO Employees(first_name,last_name,department_id)
VALUES ('Rahul','Sharma',101),
	   ('Priya','Mehta',102),
	   ('Ankit','Verma',103),
	   ('Simran','Kaur',NULL),
	   ('Aman','Singh',101);

SELECT * FROM Employees;

CREATE TABLE Departments(
	department_id INT PRIMARY KEY,
	department_name VARCHAR(50)
);

INSERT INTO Departments(department_id,department_name)
VALUES (101,'Sales'),
(102,'Marketing'),
(103,'IT'),
(104,'HR');

SELECT * FROM Departments;

-- 1 : INNER JOIN -- Retrieve Employees and theor department names where a match exists
SELECT e.employee_id,e.first_name,e.last_name,
	   d.department_id,d.department_name
FROM Employees e
INNER JOIN
Departments d
ON e.department_id = d.department_id;


-- 2 : LEFT JOIN -- Retrieve all employees and thier department names,including those without a department
SELECT e.employee_id,e.first_name,e.last_name,
	   d.department_id,d.department_name
FROM Employees e
LEFT JOIN
Departments d
ON e.department_id = d.department_id;

-- 3 : RIGHT JOIN -- Retrieve all departments and the employees working, including departments without
SELECT e.employee_id,e.first_name,e.last_name,
	   d.department_id,d.department_name
FROM Employees e
RIGHT JOIN
Departments d
ON e.department_id = d.department_id;


-- 4 : FULL OUTER JOIN -- Retrieve all employees and departments,including non-matching records from both tables
SELECT e.employee_id,e.first_name,e.last_name,
	   d.department_id,d.department_name
FROM Employees e
FULL OUTER JOIN
Departments d
ON e.department_id = d.department_id;

-- 5 : CROSS JOIN -- Retrieve all possible combinations of employees and departments.
SELECT e.first_name,e.last_name,
	   d.department_name
FROM Employees e
CROSS JOIN
Departments d;


-- 6 : SELF JOIN : FInd employees who share the same department.
SELECT e1.first_name AS Employee_name1,
	   e2.first_name AS Employee_name2
	   
FROM Employees e1 JOIN Employees e2
ON e1.department_id = e2.department_id AND e1.employee_id <> e2.employee_id
JOIN departments d
ON e1.department_id = d.department_id;




