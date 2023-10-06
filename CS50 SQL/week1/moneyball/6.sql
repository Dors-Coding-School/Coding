SELECT teams.name, SUM(performances.H) AS 'total hits' FROM teams
JOIN performances ON performances.team_id = teams.id
WHERE performances.year = 2001
GROUP BY teams.name
ORDER BY SUM(performances.H) DESC
LIMIT 5;
