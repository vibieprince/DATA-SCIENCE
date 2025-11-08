-- drop the table if it already exists
DROP TABLE IF EXISTS employees;

-- Create the employees table
CREATE TABLE employees(
	employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	department VARCHAR(30),
	salary DECIMAL(10,2) CHECK (salary>0),
	joining_date DATE NOT NULL,
	age INT CHECK (age>=18)
);

SELECT * FROM employees ORDER BY employee_id ASC;

-- Insert Data into employees table
INSERT INTO employees(first_name,last_name,department,salary,joining_date,age) VALUES
('Amit','Sharma','IT',60000.00,'2022-05-01',29),
('Neha','Patel','HR',55000.00,'2021-')