-- Step 1: Create a temporary table to import data
CREATE TABLE "meteorites_temp" (
    "name" TEXT,
    "id" INTEGER,
    "nametype" TEXT,
    "class" TEXT,
    "mass" REAL,
    "discovery" TEXT,
    "year" INTEGER,
    "lat" REAL,
    "long" REAL,
    PRIMARY KEY ("id")
);

-- Import CSV into temporary table
.import --csv --skip 1 meteorites.csv meteorites_temp

-- Step 2: Clean the imported data

-- Round mass, latitude, and longitude columns to nearest hundredth
UPDATE "meteorites_temp"
SET "mass" = ROUND("mass", 2),
    "lat" = ROUND("lat", 2),
    "long" = ROUND("long", 2);

-- Set empty values to NULL for mass, year, lat, and long columns
UPDATE "meteorites_temp"
SET "mass" = NULL
WHERE "mass" = 0;

UPDATE "meteorites_temp"
SET "year" = NULL
WHERE "year" = 0;

UPDATE "meteorites_temp"
SET "year" = NULL
WHERE TRIM("year") = '';

UPDATE "meteorites_temp"
SET "lat" = NULL
WHERE "lat" = 0;

UPDATE "meteorites_temp"
SET "long" = NULL
WHERE "long" = 0;

-- Step 3: Create final table structure
CREATE TABLE "meteorites" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT,
    "class" TEXT,
    "mass" REAL,
    "discovery" TEXT,
    "year" INTEGER,
    "lat" REAL,
    "long" REAL
);

-- Transfer clean data from temporary table to final table, excluding "Relict" and sorting by year and name
INSERT INTO "meteorites" ("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", "mass", "discovery", "year", "lat", "long"
FROM "meteorites_temp"
WHERE "nametype" NOT LIKE "%relict%"
ORDER BY "year", "name";
