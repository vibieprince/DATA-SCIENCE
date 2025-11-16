Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int)
Truncate table Activity
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5')
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-02', '6')
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1')
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0')
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5')

-- Write your MySQL query statement below
SELECT ROUND(COUNT(DISTINCT player_id)/ (SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS fraction
FROM Activity
WHERE (player_id,DATE_SUB(event_date,INTERVAL 1 DAY)) IN (
    SELECT player_id,MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)

-- Write your PostgreSQL query statement below
SELECT 
  ROUND(
    COUNT(DISTINCT player_id)::numeric / 
    (SELECT COUNT(DISTINCT player_id) FROM Activity),
    2
  ) AS fraction
FROM Activity a
WHERE (a.player_id, a.event_date - INTERVAL '1 day') IN (
    SELECT 
      player_id,
      MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
);
2