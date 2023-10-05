SELECT latitude, longitude, "0m" AS "surface temperature"
FROM normals
ORDER BY "0m" DESC, latitude
LIMIT 10;
