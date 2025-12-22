WITH RECURSIVE my_cte AS (
    SELECT 1 AS n 
    UNION ALL
    SELECT n+2 FROM my_cte 
    WHERE n < 5
)

SELECT * FROM my_cte 

-- 1
-- 3
-- 5