Create table If Not Exists Logs (id int, num int)
Truncate table Logs
insert into Logs (id, num) values ('1', '1')
insert into Logs (id, num) values ('2', '1')
insert into Logs (id, num) values ('3', '1')
insert into Logs (id, num) values ('4', '2')
insert into Logs (id, num) values ('5', '1')
insert into Logs (id, num) values ('6', '2')
insert into Logs (id, num) values ('7', '2')

-- Code 1 : Write your PostgreSQL query statement below
SELECT l1.num  AS ConsecutiveNums 
FROM Logs l1,Logs l2,Logs l3
WHERE l1.id - l2.id = 1
AND l2.id - l3.id = 1
AND l1.num = l2.num
AND l2.num = l3.num
AND l1.num = l3.num
GROUP BY l1.num

-- jo bhi number hai consecutive uski id's ka difference sirf 1 hoga?? right

-- Code 2 : Write your PostgreSQL query statement below
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id - 1
JOIN Logs l3 ON l2.id = l3.id - 1
WHERE l1.num = l2.num AND l2.num = l3.num;