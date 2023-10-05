SELECT latitude, longitude, "0m" AS "surface temperature"
FROM normals
ORDER BY "0m", latitude
LIMIT 10;
