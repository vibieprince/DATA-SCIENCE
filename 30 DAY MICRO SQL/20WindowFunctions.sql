SELECT new_id,new_cat,
    SUM(new_id) OVER(PARTITION BY new_cat ORDER BY new_id) AS "Total",
    AVG(new_id) OVER(PARTITION BY new_cat ORDER BY new_id) AS "Average",
    COUNT(new_id) OVER(PARTITION BY new_cat ORDER BY new_id) AS "Count",
    MIN(new_id) OVER(PARTITION BY new_cat ORDER BY new_id) AS "Min",
    MAX(new_id) OVER(PARTITION BY new_cat ORDER BY new_id) AS "Max",
FROM test_data