-- List all genres not linked to the show Dexter
SELECT c.name
FROM tv_shows AS a
JOIN tv_show_genres AS b
ON a.id = b.show_id
JOIN tv_genres AS c
ON b.genre_id = c.id
WHERE a.title = 'Dexter'
ORDER BY c.name ASC;
