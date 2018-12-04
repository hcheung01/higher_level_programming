-- Displays the top 3 of cities temperature during JULY and August
SELECT city, AVG(value) as avg_temp from temperatures WHERE month IN (7, 8) GROUP BY CITY ORDER BY avg_temp DESC LIMIT 3;
