CREATE VIEW "by_district" AS
SELECT district, SUM(families), sum(households), SUM(population), SUM(male), SUM(female) FROM "census"
GROUP BY district;
