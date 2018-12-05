-- Lists all genres from a database and displays the number of shows linked
SELECT a.name AS genre, COUNT(b.genre_id) AS number_of_shows
FROM tv_genres a
INNER JOIN tv_show_genres b
ON a.id = b.genre_id
GROUP BY b.genre_id
ORDER BY number_of_shows DESC;
