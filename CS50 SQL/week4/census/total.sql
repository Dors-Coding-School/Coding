CREATE VIEW "total" AS
SELECT SUM(families), sum(households) AS "households", SUM(population), SUM(male), SUM(female) FROM "census";
