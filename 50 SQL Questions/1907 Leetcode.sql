Create table If Not Exists Accounts (account_id int, income int)
Truncate table Accounts
insert into Accounts (account_id, income) values ('3', '108939')
insert into Accounts (account_id, income) values ('2', '12747')
insert into Accounts (account_id, income) values ('8', '87709')
insert into Accounts (account_id, income) values ('6', '91796')

SELECT category, accounts_count
FROM (
    SELECT 'Low Salary' AS category, 
           COUNT(*) AS accounts_count
    FROM Accounts
    WHERE income < 20000

    UNION ALL

    SELECT 'Average Salary' AS category, 
           COUNT(*) AS accounts_count
    FROM Accounts
    WHERE income BETWEEN 20000 AND 50000

    UNION ALL

    SELECT 'High Salary' AS category, 
           COUNT(*) AS accounts_count
    FROM Accounts
    WHERE income > 50000
) AS t
ORDER BY 
    CASE category
        WHEN 'High Salary' THEN 1
        WHEN 'Low Salary' THEN 2
        WHEN 'Average Salary' THEN 3
    END;
