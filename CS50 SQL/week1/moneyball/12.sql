SELECT players.first_name, players.last_name
FROM players
JOIN salaries ON salaries.player_id = players.id
JOIN performances ON performances.player_id = players.id AND performances.year = salaries.year
WHERE salaries.year = 2001 AND performances.H > 0 AND performances.RBI > 0
AND (salaries.salary/performances.H) IN (
    SELECT salary/H
    FROM salaries
    JOIN performances ON performances.player_id = salaries.player_id AND performances.year = salaries.year
    WHERE salaries.year = 2001 AND H > 0
    ORDER BY salary/H ASC
    LIMIT 10
)
AND (salaries.salary/performances.RBI) IN (
    SELECT salary/RBI
    FROM salaries
    JOIN performances ON performances.player_id = salaries.player_id AND performances.year = salaries.year
    WHERE salaries.year = 2001 AND RBI > 0
    ORDER BY salary/RBI ASC
    LIMIT 10
)
ORDER BY players.last_name, players.first_name;
