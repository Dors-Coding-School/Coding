SELECT DISTINCT districts.city, AVG(per_pupil_expenditure) as 'Average Per Pupil Expenditure' FROM expenditures
JOIN districts ON districts.id = expenditures.district_id
GROUP BY districts.city
ORDER BY AVG(per_pupil_expenditure) DESC;
