SELECT * FROM employees;
-- 1 : Retrieve the first_name,salary and calculate a 10% bonus on the salary
SELECT first_name,salary, (salary*0.10) AS Bonus FROM employees;

-- 2 : Caculate the annual salary and salary increment by 5% - show the monthly new salary as well
SELECT first_name,last_name,monthly_salary,
	(monthly_salary*12.0) AS annual_salary,
	(monthly_salary*0.05) AS increment_amount,
	(monthly_salary + monthly_salary*0.05) as new_salary
FROM employees;

ALTER TABLE employees
RENAME COLUMN salary TO monthly_salary;

-- 3 : retrieve all the employees above age 30
SELECT first_name,last_name,age FROM employees
WHERE age > 30;

-- 4 : retrieve all the employees whose salary is above 50000
SELECT first_name,last_name,monthly_salary FROM employees
WHERE monthly_salary > 50000;

-- 5 : retrieve all the employees whose salary is above 50000 and age is above 40
SELECT first_name,last_name,monthly_salary FROM employees
WHERE monthly_salary > 50000 AND age > 40;

-- 6 : Retrieve employees whose salary is between 40,000 and 60,000. - use BETWEEN Operators
SELECT first_name,last_name,monthly_salary FROM employees
WHERE monthly_salary BETWEEN 40000 AND 60000;

-- 7 : Find the employees whose email address end with @gmail.com - Use LIKE Operators
SELECT first_name,last_name,email FROM employees
WHERE email LIKE '%@gmail.com';

-- 8 : Retrieve the employees who belong to either the 'Finance' or 'Marketing' departments -- USe IN Operator
SELECT first_name,last_name,dept_name FROM employees
WHERE dept_name IN ('Finance','Marketing');

-- 9 : Find the employees where the email column is NULL (if applicable)
SELECT first_name,last_name,email FROM employees
WHERE email IS NULL;

-- 10 : List employees sorted by salary in DESCENDING order
SELECT first_name,last_name,monthly_salary
FROM employees
ORDER BY monthly_salary ASC;

-- 11 : Retrieve a list of top 5 highest paid employees
SELECT first_name,last_name,monthly_salary
FROM employees
ORDER BY monthly_salary DESC
LIMIT 5;

-- 12 : Retrieve list of unique departments
SELECT COUNT (DISTINCT dept_name) AS departments
FROM employees;
