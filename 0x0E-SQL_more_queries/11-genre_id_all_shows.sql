-- Lists all shows contained in a database
SELECT a.title, b.genre_id
FROM tv_shows AS a
LEFT JOIN tv_show_genres AS b
ON a.id = b.show_id
ORDER BY a.title ASC, b.genre_id ASC;
