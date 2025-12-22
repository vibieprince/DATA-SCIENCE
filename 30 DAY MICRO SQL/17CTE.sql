-- Common Table Query 

WITH my_cte AS (
    SELECT *, AVG(amount) OVER (ORDER BY p.customer_id) AS "Average_Price",
    COUNT(address_id) OVER (ORDER BY c.customer_id) AS "Count"
    FROM payment AS p
    INNER JOIN customer AS c
    ON c.customer_id = p.customer_id
) -- ab ye result my_cte ke andar store ho jayega

SELECT first_name,last_name
FROM my_cte -- ab hum data my_cte table se le rahe hain

-- Dual Common Table Query
WITH my_cp AS ( -- customer payment ke liye CTE
    SELECT *, AVG(amount) OVER (ORDER BY p.customer_id) AS "Average_Price",
    COUNT(address_id) OVER (ORDER BY c.customer_id) AS "Count"
    FROM payment AS p
    INNER JOIN customer AS c
    ON c.customer_id = p.customer_id
),
my_ca AS ( -- customer address ke liye CTE
    SELECT *
    FROM customer AS c
    INNER JOIN address AS a 
    ON a.address_id = c.address_id
    INNER JOIN country AS cc 
    ON cc.city_id = a.city_id
)

SELECT cp.first_name,cp.last_name,ca.city,ca.country,cp.amonut 
FROM my_ca AS ca, my_cp AS cp 