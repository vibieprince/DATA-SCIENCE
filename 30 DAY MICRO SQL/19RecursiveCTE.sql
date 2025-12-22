-- practical example for recursive cte
CREATE TABLE employees(
    emp_id SERIAL PRIMARY KEY,
    emp_name VARCHAR NOT NULL,
    manager_id INT
);

INSERT INTO employees(emp_id,emp_name,manager_id)
VALUES(1,'Madhav',NULL),
(2,'Sam',1),
(3,'Tom',2),
(4,'Arjun',6),
(5,'Shiva',4),
(6,'Keshav',1),
(7,'Damodar',5);

SELECT * FROM employees

WITH RECURSIVE EmpCTE AS(
    SELECT emp_id,emp_name,manager_id
    FROM employees
    WHERE emp_id = 7

    UNION ALL 

    SELECT e.emp_id,e.emp_name,e.manager_id
    FROM employees
    JOIN EmpCTE
    ON e.emp_id = EmpCTE.manager_id 
)

SELECT * FROM EmpCTE 
