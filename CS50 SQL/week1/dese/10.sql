SELECT districts.name, expenditures.per_pupil_expenditure FROM expenditures
JOIN districts ON districts.id = expenditures.district_id
WHERE type LIKE '%Public School%'
ORDER BY expenditures.per_pupil_expenditure DESC
LIMIT 10;
