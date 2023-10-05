SELECT latitude, longitude, "50m" AS temperature
FROM normals
WHERE latitude BETWEEN 0 AND 20
AND longitude BETWEEN 55 AND 75;
