-- Real, CTE based question
WITH my_cte AS(
    SELECT mode,MAX(amount) AS highest_price,SUM(amount) AS total_price
    FROM payment 
    GROUP BY mode
)

SELECT payment.*,my.highest_price,my.total_price
FROM payment
JOIN my_cte my 
ON payment.mode = my.mode 
ORDER BY payment.mode 