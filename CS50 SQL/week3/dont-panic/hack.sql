-- 1. Alter the password of the 'admin' account
-- The MD5 hash for "oops!" is 982c0381c279d139fd221fce974916e7 (You can find this from md5hashgenerator.com).
UPDATE "users"
SET "password" = '982c0381c279d139fd221fce974916e7'
WHERE "username" = 'admin';

-- 2. Erase any logs of your activity
DELETE FROM "user_logs";

-- 3. Add false data
-- First, get the password for 'emily33'
INSERT INTO "user_logs" ("type", "old_username", "new_username", "old_password", "new_password")
SELECT 'update', 'admin', 'admin', "password", "password"
FROM "users"
WHERE "username" = 'emily33';
