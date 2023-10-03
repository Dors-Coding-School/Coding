SELECT english_title, artist FROM views
WHERE english_title LIKE "%Fuji%"
ORDER BY brightness DESC
LIMIT 1;
