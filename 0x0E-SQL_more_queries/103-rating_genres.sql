-- Lists all genres in the database by their rating
SELECT a.name, SUM(c.rate) AS rating
FROM tv_genres AS a
JOIN tv_show_genres AS b
ON a.id = b.genre_id
JOIN tv_show_ratings AS c
ON b.show_id = c.show_id
GROUP BY a.name
ORDER BY rating DESC;
