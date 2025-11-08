DROP TABLE IF EXISTS users;
CREATE TABLE users(
	user_id INT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	email VARCHAR(100) UNIQUE,
	age INTEGER CHECK (age >= 18),
	reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Inserting data into table
INSERT INTO users (user_id,name,email,age)
VALUES (1,'John Doe','john.doe@example.com',25);

INSERT INTO users (user_id,name,email,age)
VALUES (2,'John Doe','john1.doe@example.com',25);

SELECT * FROM users;