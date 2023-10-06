SELECT teams.name, ROUND(AVG(salaries.salary),2) FROM salaries
JOIN teams ON teams.id = salaries.team_id
WHERE salaries.year = 2001
GROUP BY teams.name
ORDER BY ROUND(AVG(salaries.salary),2) ASC
LIMIT 5;
