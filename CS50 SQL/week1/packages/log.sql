
-- *** The Lost Letter ***
-- Check if Anneke address is correct
SELECT id FROM addresses
WHERE address LIKE '%900 Somerville Avenue%';

-- Check if Varsha address is correct
SELECT * FROM addresses
WHERE address LIKE '%Finn%';

-- Get Package Content
SELECT * FROM packages
WHERE from_address_id = (
    SELECT id FROM addresses
    WHERE address LIKE '%900 Somerville Avenue%'
) AND to_address_id = (
    SELECT id FROM addresses
    WHERE address LIKE '%Finn%'
);

-- Get info about scans
SELECT * FROM scans
WHERE package_id = (
    SELECT id FROM packages
        WHERE from_address_id = (
            SELECT id FROM addresses
            WHERE address LIKE '%900 Somerville Avenue%'
        ) AND to_address_id = (
            SELECT id FROM addresses
            WHERE address LIKE '%Finn%'
        )
    );

-- Get address and type delivered
SELECT type, address FROM addresses
WHERE id = (
    SELECT address_id FROM scans
    WHERE package_id = (
        SELECT id FROM packages
            WHERE from_address_id = (
                SELECT id FROM addresses
                WHERE address LIKE '%900 Somerville Avenue%'
            ) AND to_address_id = (
                SELECT id FROM addresses
                WHERE address LIKE '%Finn%'
            ) AND action = 'Drop'
    )
);

-- *** The Devious Delivery ***
--  Afraid there’s no “From” address:
SELECT * FROM packages
WHERE from_address_id IS NULL;

-- SCANS
SELECT * FROM scans
WHERE package_id = (
    SELECT id FROM packages
    WHERE from_address_id IS NULL
);

SELECT type, address FROM addresses
WHERE id = (
    SELECT address_id FROM scans
    WHERE package_id = (
        SELECT id FROM packages
        WHERE from_address_id IS NULL
    ) AND action = 'Drop'
);

-- *** The Forgotten Gift ***
-- Get id of grandparent
SELECT id FROM addresses
WHERE address = '109 Tileston Street';

-- Get id of granddaughter
SELECT id FROM addresses
WHERE address = '728 Maple Place';

-- Info about package
SELECT * FROM packages
WHERE from_address_id = (
    SELECT id FROM addresses
    WHERE address = '109 Tileston Street'
) AND to_address_id = (
    SELECT id FROM addresses
    WHERE address = '728 Maple Place'
);

-- Scans
SELECT * FROM scans
WHERE package_id = (
    SELECT id FROM packages
    WHERE from_address_id = (
        SELECT id FROM addresses
        WHERE address = '109 Tileston Street'
    ) AND to_address_id = (
        SELECT id FROM addresses
        WHERE address = '728 Maple Place'
    )
);

-- Driver name
SELECT name FROM drivers
WHERE id = (
    SELECT driver_id FROM scans
    WHERE package_id = (
        SELECT id FROM packages
        WHERE from_address_id = (
            SELECT id FROM addresses
            WHERE address = '109 Tileston Street'
        ) AND to_address_id = (
            SELECT id FROM addresses
            WHERE address = '728 Maple Place'
        )
    )
    ORDER BY timestamp DESC
    LIMIT 1
);
