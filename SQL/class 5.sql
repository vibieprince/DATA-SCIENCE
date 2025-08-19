CREATE DATABASE Office;
USE Office;
CREATE TABLE workers(
	id INT PRIMARY KEY,
    name VARCHAR(50),
    slary INT NOT NULL,
    city VARCHAR(40)
);

INSERT INTO workers VALUES (101,"Prince",100000,"Noida"),(102,"Akash",30000,"Azamgarh"),(103,"Aman",70000,"Gopalganj"),(104,"Abhishek",10000,"Kuleshra");

SELECT * FROM workers WHERE id > 102 LIMIT 3;

SELECT * FROM workers ORDER BY city ASC;


SELECT max(slary) FROM workers;

SELECT avg(slary) FROM workers;

SELECT count(slary) FROM workers;

SELECT city, count(id) FROM workers GROUP BY city;