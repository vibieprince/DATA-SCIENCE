SELECT * FROM products;

-- Get current date and time
SELECT NOW() AS current_datetime;

-- get current date
SELECT CURRENT_DATE AS today_date;

SELECT added_date,current_date,(CURRENT_DATE - added_date) AS days_diff
FROM products;

-- Extract parts of a date
-- Extract the year months and day from the added_date column.
SELECT product_name, 
	EXTRACT(YEAR FROM added_date) AS year_added,
	EXTRACT(MONTH FROM added_date) AS month,
	EXTRACT(DAY FROM added_date) AS year_added
FROM products;

-- Calculate the age between date
-- Calculate the time_difference between added_date and today's date
SELECT product_name,
	AGE(CURRENT_DATE,added_date) AS age_since_added
FROM products;

-- Format dates as strings
SELECT product_name,
	TO_CHAR(added_date,'DD-Mon-YYYY') AS age_since_added
FROM products;