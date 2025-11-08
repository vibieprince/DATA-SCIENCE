-- 1 : Retrieve the first_name,salary and calculate a 10% bonus on the salary
SELECT first_name,salary, (salary*0.10) AS Bonus FROM employees;

-- 2 : Caculate the annual salary and salary increment by 5% - show the monthly new salary as well
SELECT first_name,last_name,salary
	(salary*12.0) AS annual_salary,
	(salary*0.05) AS increment_amount,
	(salary*0.05) AS new_salary,
	(salary + salary*0.05) as new_sa
FROM employees;