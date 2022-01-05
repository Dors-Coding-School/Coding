-- Keep a log of any SQL queries you execute as you solve the mystery.
--All you know is that the theft took place on July 28, 2020 and that it took place on Chamberlin Street.
SELECT description
FROM crime_scene_reports
WHERE day=28 AND month=7 AND year=2020 AND street="Chamberlin Street"

--Work with the description
SELECT transcript
FROM interviews
WHERE day = "28" AND month = "7" AND year = "2020" AND transcript like "%courthouse%"

--Working with the first transcript:
--"Sometime within ten minutes of the theft, I saw the thief get into a car in the courthouse
--parking lot and drive away. If you have security footage from the courthouse parking lot,
--you might want to look for cars that left the parking lot in that time frame."
SELECT name
FROM people
JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE day = "28" AND month = "7" AND year = "2020" AND hour = "10" AND minute >= "15" AND minute < "25" AND activity = "exit"

--Suspects: Patrick, Ernest, Amber, Danielle, Roger, Elizabeth, Russel, Evelyn


--Working with the second transcript:
--"I don't know the thief's name, but it was someone I recognized. Earlier this morning,
--before I arrived at the courthouse, I was walking by the ATM on Fifer Street and saw
--the thief there withdrawing some money."
SELECT DISTINCT name
FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE day = "28" AND month = "7" AND year = "2020" AND transaction_type = "withdraw" AND atm_location = "Fifer Street"

--Suspects: Danielle, Bobby, Madison, Ernest, Roy, Elizabeth, Victoria, Russel

--By now, the names that appeared in both cases are: Ernest, Danielle, Elizabeth, Russel

--Working with the third transcript:
--"As the thief was leaving the courthouse, they called someone who talked to them for less than a minute.
--In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville
--tomorrow.The thief then asked the person on the other end of the phone to purchase the flight ticket."
--First check the passengers for the flight
SELECT name
FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id = (
    SELECT id
    FROM flights
    WHERE day = "29" AND month = "7" AND year = "2020"
    ORDER BY hour, minute
    LIMIT 1)
--Suspects: Doris, Roger, Ernest, Edward, Evelyn, Madison, Bobby, Danielle
--By now, our main suspects are: Ernest and Danielle

--Check the phone calls
SELECT DISTINCT name
FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE day = "28" AND month = "7" AND year = "2020" AND duration < "60"
--Suspects: Roger, Evelyn, Ernest, Madison, Russell, Kimberly, Bobby, Victoria

--The thief is Ernest!

SELECT city
FROM airports
WHERE id = (
    SELECT destination_airport_id
    FROM flights
    WHERE day = "29" AND month = "7" AND year = "2020"
    ORDER BY hour, minute
    LIMIT 1)
--The thief ESCAPED TO: London

--Now we have to get "The ACCOMPLICE is":
SELECT name
FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE day = "28" AND month = "7" AND year = "2020" AND duration < "60" AND caller = (
    SELECT phone_number
    FROM people
    WHERE name = "Ernest");
--The ACCOMPLICE is: Berthold
