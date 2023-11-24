SELECT id, description
FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';
SELECT id, transcript
FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28;
SELECT people.name AS Suspect
FROM people JOIN bank_accounts
ON people.id = bank_accounts.person_id
WHERE bank_accounts.account_number IN
(
    SELECT account_number
    FROM atm_transactions
    WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
)
AND people.phone_number IN
(
    SELECT caller
    FROM phone_calls
    WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
)
AND people.license_plate IN
(
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 OR minute <= 25) AND activity = 'exit'
)
AND people.passport_number IN
(
    SELECT passport_number
    FROM passengers
    WHERE flight_id IN
    (
        SELECT id
        FROM flights
        WHERE year = 2021 AND month = 7 AND day = 29
        AND origin_airport_id IN
        (
            SELECT id
            FROM airports
            WHERE city = 'Fiftyville'
        )
    )
)
;
SELECT people.name as Accomplice
FROM people JOIN phone_calls
ON people.phone_number = phone_calls.receiver
WHERE phone_calls.duration < 60
AND phone_calls.caller IN
(
    SELECT phone_number
    FROM people
    WHERE (name = 'Bruce' OR name = 'Diana' OR name = 'Taylor')
)
;
SELECT full_name, city
FROM airports
WHERE id IN
(
    SELECT destination_airport_id
    FROM flights JOIN passengers
    ON flights.id = passengers.flight_id
    WHERE flights.year = 2021 AND flights.month = 7 AND flights.day = 29
    AND passengers.passport_number IN
    (
        SELECT passport_number
        FROM people
        WHERE name = 'Bruce'
    )
    AND flights.origin_airport_id IN
    (
        SELECT id
        FROM airports
        WHERE city = 'Fiftyville'
    )
)
;