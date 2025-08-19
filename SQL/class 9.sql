CREATE TABLE employee(
	id INT PRIMARY KEY,
    name VARCHAR(50),
    manager_id INT
);

INSERT INTO employee (id,name,manager_id)
VALUES
(101,"Adam",103),
(102,"Bob",104),
(103,"Casey",NULL),
(104,"Donald",103);

SELECT * FROM employee;

SELECT a.name as manager_name,b.name
FROM employee as a
JOIN employee as b
ON a.id = b.manager_id;