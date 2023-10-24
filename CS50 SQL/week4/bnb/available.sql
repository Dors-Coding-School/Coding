CREATE VIEW "available" AS
SELECT listings.id, listings.property_type, listings.host_name, availabilities.date FROM listings
JOIN availabilities ON listings.id = availabilities.listing_id
WHERE available = "TRUE";
