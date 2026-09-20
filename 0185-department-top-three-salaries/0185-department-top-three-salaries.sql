# Write your MySQL query statement below
WITH CTE AS (SELECT e.id, e.name as Employee, e.salary as Salary, d.name as Department ,
       DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS pay
FROM Employee AS e
JOIN Department AS d
ON e.departmentId = d.id)

SELECT Department,Employee,Salary
FROM CTE
WHERE pay<=3