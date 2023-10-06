SELECT city, COUNT(name) AS public_school_count
FROM schools
WHERE type = 'Public School'
GROUP BY city
ORDER BY public_school_count DESC, city ASC
LIMIT 10;
