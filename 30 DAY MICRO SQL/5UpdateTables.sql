DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users(
	user_id SERIAL PRIMARY KEY,
	username VARCHAR(50) NOT NULL,
	email VARCHAR(100) UNIQUE,
	age INT,
	city VARCHAR(50)
);

SELECT * FROM users;

INSERT INTO users (username,email,age,city) VALUES
('Akash','akash@gmail.com',22,'Azamgarh'),
('Anchal','anchal@gmail.com',19,'Mumbai'),
('Prince','prince@gmail.com',21,'Noida');

DELETE FROM users
WHERE user_id IN (1,2,3);

UPDATE users
SET age = 26
WHERE username = 'Prince';

SELECT * FROM users ORDER BY username ASC;

UPDATE users
SET age=31,city='Kolkata'
WHERE username = 'Anchal';

UPDATE users
SET email = 'akash@yahoo.com'
WHERE username = 'Akash';

UPDATE users
SET age = age+1
WHERE email LIKE '%@yahoo.com';