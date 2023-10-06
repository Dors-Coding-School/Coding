SELECT DISTINCT teams.name FROM teams
JOIN performances ON performances.team_id = teams.id
JOIN players ON players.id = performances.player_id
WHERE players.first_name = 'Satchel' AND players.last_name = 'Paige';
