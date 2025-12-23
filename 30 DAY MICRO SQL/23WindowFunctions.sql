SELECT new_id,
    FIRST_VALUE(new_id) OVER(ORDER BY new_id) AS "FIRST_VALUE",
    LAST_VALUE(new_id) OVER(ORDER BY new_id) AS "LAST_VALUE",
    LEAD(new_id) OVER(ORDER BY new_id) AS "LAST_VALUE", -- matlab next value, i.e last row pe null dega
    LAG(new_id) OVER(ORDER BY new_id) AS "LAG" -- matlab prev value, i.e first row pe null dega
FROM test_data

-- NOTE: If you want the single last value from whole column, use: "ROWS BETWEEN UNBOUNDED PRECEEDING AND UNBOUNDED FOLLOWING"


SELECT new_id,
    LEAD(new_id,2) OVER(ORDER BY new_id) AS "LEAD_by2",
    LAG(new_id,2) OVER(ORDER BY new_id) AS "LEAD_by2"
FROM test_data
