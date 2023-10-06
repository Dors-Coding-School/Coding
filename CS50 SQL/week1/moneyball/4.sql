SELECT first_name, last_name, salary FROM players
JOIN salaries ON salaries.player_id = players.id
WHERE year = 2001
ORDER BY salary ASC, first_name ASC, last_name ASC, players.id ASC
LIMIT 50;
