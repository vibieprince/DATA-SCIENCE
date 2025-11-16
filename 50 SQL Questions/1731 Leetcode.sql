Create table If Not Exists Employees(employee_id int, name varchar(20), reports_to int, age int)
Truncate table Employees
insert into Employees (employee_id, name, reports_to, age) values ('9', 'Hercy', NULL, '43')
insert into Employees (employee_id, name, reports_to, age) values ('6', 'Alice', '9', '41')
insert into Employees (employee_id, name, reports_to, age) values ('4', 'Bob', '9', '36')
insert into Employees (employee_id, name, reports_to, age) values ('2', 'Winston', NULL, '37')

-- Write your PostgreSQL query statement below
SELECT 
    man.employee_id,
    man.name,
    COUNT(emp.employee_id) AS reports_count,
    ROUND(AVG(emp.age)) AS average_age
FROM Employees emp
JOIN Employees man
    ON emp.reports_to = man.employee_id
GROUP BY man.employee_id, man.name
ORDER BY man.employee_id;