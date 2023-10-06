SELECT districts.name, expenditures.pupils FROM expenditures
JOIN districts ON districts.id = expenditures.district_id;
