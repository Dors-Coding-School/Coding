CREATE VIEW "frequently_reviewed" AS
SELECT listings.id, listings.property_type, listings.host_name FROM listings
JOIN reviews ON listings.id = reviews.listing_id
GROUP BY reviews.listing_id
ORDER BY COUNT(reviews.listing_id) DESC, property_type, host_name
LIMIT 100;
