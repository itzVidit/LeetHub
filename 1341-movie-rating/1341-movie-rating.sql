# Write your MySQL query statement below
(SELECT name as results 
FROM Users as u
JOIN MovieRating as m 
ON u.user_id = m.user_id
GROUP BY u.user_id
ORDER BY count(u.user_id) DESC , name ASC 
LIMIT 1)

UNION ALL

(SELECT m.title as results
FROM Movies as m 
JOIN MovieRating as mr
ON m.movie_id = mr.movie_id
WHERE mr.created_at LIKE '2020-02-%'
GROUP BY m.movie_id
ORDER BY AVG(mr.rating) DESC , m.title ASC
LIMIT 1 )