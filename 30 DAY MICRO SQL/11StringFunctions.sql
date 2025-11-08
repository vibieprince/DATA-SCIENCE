SELECT * FROM products;

-- Get all categories in Upper case
SELECT UPPER(category) AS Category_CAP
FROM products;

-- Get all categories in lower case
SELECT LOWER(category) AS Category_LOW
FROM products;

-- Join Product_name and category text with hypen
SELECT CONCAT(product_name,'_',Category) AS product_details
FROM products;

-- Extract the first 5 characters from product_name
SELECT SUBSTRING(product_name,1,5) AS short_name
FROM products;

-- Count Length
SELECT product_name,LENGTH(product_name) AS countOfChar
FROM products;

-- Remove leading and trailing spaces from string
SELECT LENGTH(TRIM('   Monitor    ')) AS trimmed_text;
SELECT LENGTH('   Monitor    ') AS trimmed_text;

-- Replace the word "Phone" with "device" in product names
SELECT REPLACE (product_name,'phone','device') AS updated
FROM products;

-- Get first 3 characters from category
SELECT RIGHT(category,3) AS Category_CAP
FROM products;