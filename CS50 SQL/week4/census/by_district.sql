CREATE VIEW "by_district" AS
SELECT district, SUM(families) as "families", sum(households), SUM(population), SUM(male), SUM(female) FROM "census"
GROUP BY district;
