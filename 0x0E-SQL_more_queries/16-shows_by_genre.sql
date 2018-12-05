-- List all shows and all genres linked to a show
SELECT a.title, c.name
FROM tv_shows AS a
LEFT JOIN tv_show_genres AS b
ON a.id = b.show_id
LEFT JOIN tv_genres AS c
ON b.genre_id = c.id
ORDER BY a.title ASC, c.name ASC;
