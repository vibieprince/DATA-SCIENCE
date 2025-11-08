SELECT * FROM products;

ALTER TABLE products
ADD COLUMN discounted_price NUMERIC(10,2);

UPDATE products SET discounted_price = price*0.9
WHERE product_name NOT IN ('Laptop','Desk');


SELECT product_name,
	COALESCE(discounted_price,price) AS final_price
FROM products;