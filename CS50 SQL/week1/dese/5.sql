SELECT city, COUNT(name) AS public_school_count
FROM schools
WHERE type = 'Public School'
GROUP BY city
HAVING public_school_count <= 3
ORDER BY public_school_count DESC, city ASC;
