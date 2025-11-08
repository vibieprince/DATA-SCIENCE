SELECT * FROM products;

-- Assign a unique row number to each product within the same category
SELECT product_name,category,price,
	ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) AS row_num
FROM products;

-- DENSE_RANK () -- duplicacy mein ranking mein kaam aata hai

SELECT product_name,category,price,
	SUM(price) OVER(ORDER BY price DESC) AS Running_total
FROM products;