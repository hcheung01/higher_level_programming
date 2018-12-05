-- Lists all shows contained in database with at least one genre linked
SELECT a.title, b.genre_id
FROM tv_shows AS a, tv_show_genres AS b
WHERE b.show_id = a.id
ORDER BY a.title ASC, b.genre_id ASC;
