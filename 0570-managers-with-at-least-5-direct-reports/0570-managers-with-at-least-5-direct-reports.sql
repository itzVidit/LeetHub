# Write your MySQL query statement below
SELECT e1.name 
FROM employee as e1
JOIN employee as e2 
ON e1.id = e2.managerId
GROUP BY e2.managerId
having count(e2.managerId)>=5