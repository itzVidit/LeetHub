# Write your MySQL query statement below
WITH CTE AS (select requester_id id from RequestAccepted
union all
select accepter_id id from RequestAccepted)

SELECT id , count(id) num FROM CTE GROUP BY id ORDER BY num desc LIMIT 1