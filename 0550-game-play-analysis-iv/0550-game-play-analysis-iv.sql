WITH CTE AS (
    SELECT player_id, MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(
    SUM(EXISTS (
            SELECT 1
            FROM Activity a
            WHERE a.player_id = CTE.player_id
              AND a.event_date = CTE.first_date + INTERVAL 1 DAY)) / COUNT(*),2) AS fraction
FROM CTE;