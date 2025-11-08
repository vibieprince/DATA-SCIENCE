CREATE TABLE employee(
	employeeID SERIAL PRIMARY KEY,
	name VARCHAR(20)NOT NULL,
	position VARCHAR(10),
	department VARCHAR(10),
	joining_date DATE,
	salary NUMERIC(10,2)
);

SELECT * FROM employee;