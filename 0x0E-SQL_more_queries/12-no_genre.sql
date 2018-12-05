-- Lists all shows in a database with a genre linked
SELECT a.title, b.genre_id
FROM tv_shows AS a
LEFT JOIN tv_show_genres AS b
ON a.id = b.show_id
WHERE b.genre_id IS NULL
ORDER BY a.title ASC, b.genre_id ASC;
