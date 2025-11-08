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

SELECT * FROM users ORDER BY full_name ASC;

UPDATE users
SET age=31,city='Kolkata'
WHERE username = 'Anchal';

UPDATE users
SET email = 'akash@yahoo.com'
WHERE username = 'Akash';

UPDATE users
SET age = age+1
WHERE email LIKE '%@yahoo.com';

-- To rename the username column to Full_Name
ALTER TABLE users
RENAME COLUMN username TO full_name;

-- To change the age column's data type from int to SMALLINT
ALTER TABLE users
ALTER COLUMN age TYPE SMALLINT;

-- To add NOT NULL constraint to city column
ALTER TABLE users
ALTER COLUMN city SET NOT NULL;


-- Adding check constraint to age column
ALTER TABLE users
ADD CONSTRAINT age CHECK(age>=18);

ALTER TABLE users
RENAME TO customers;

SELECT * FROM customers ORDER BY user_id ASC;

