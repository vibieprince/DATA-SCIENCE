CREATE TABLE emp(
	id INT,
    salary INT DEFAULT 25000
);

INSERT INTO emp (id) VALUES (101);
SELECT * FROM emp;

CREATE TABLE city(
	id INT PRIMARY KEY,
    city VARCHAR(50),
    age INT,
    CONSTRAINT age_check CHECK (age>=18 AND city = "Delhi")
);

create TABLE newTAB(
	age INT CHECK (age>=18)
);