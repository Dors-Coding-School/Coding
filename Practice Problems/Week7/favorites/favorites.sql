UPDATE shows SET title = "How I Met Your Mother" WHERE title LIKE "How i met your mother";
UPDATE shows SET title = "Adventure Time" WHERE title LIKE "Adventure Time";
UPDATE shows SET title = "Arrow" WHERE title LIKE "Arrow";
UPDATE shows SET title = "Avatar: The Last Airbender" WHERE title LIKE "Avatar: The Last Airbender";
UPDATE shows SET title = "Brooklyn Nine-Nine" WHERE title LIKE "Brooklyn Nine-Nine";
UPDATE shows SET title = "Community" WHERE title LIKE "Community";
UPDATE shows SET title = "Family Guy" WHERE title LIKE "Family Guy";
UPDATE shows SET title = "Friends" WHERE title LIKE "Friends";
UPDATE shows SET title = "Game of Thrones" WHERE title LIKE "Game of Thrones";
UPDATE shows SET title = "Gilmore Girls" WHERE title LIKE "Gilmore Girls";
UPDATE shows SET title = "Grey's Anatomy" WHERE title LIKE "Grey's Anatomy";
UPDATE shows SET title = "It's Always Sunny in Philadelphia" WHERE title LIKE "It's Always Sunny in Philadelphia";
UPDATE shows SET title = "Parks and Recreation" WHERE title LIKE "Parks and Recreation";
UPDATE shows SET title = "Sherlock" WHERE title LIKE "Sherlock";
UPDATE shows SET title = "Squid Game" WHERE title LIKE "Squid Game";
UPDATE shows SET title = "The Bachelorette" WHERE title LIKE "The Bachelorette";
UPDATE shows SET title = "The Crown" WHERE title LIKE "The Crown";
UPDATE shows SET title = "The Office" WHERE title LIKE "The Office";
UPDATE shows SET title = "The Queen's Gambit" WHERE title LIKE "The Queen's Gambit";
UPDATE shows SET title = "The Untamed" WHERE title LIKE "The Untamed";

UPDATE shows SET title = "Brooklyn Nine-Nine" WHERE title LIKE "B99";
UPDATE shows SET title = "Brooklyn Nine-Nine" WHERE title LIKE "Brooklyn%";

UPDATE shows SET title = "Game of Thrones" WHERE title LIKE "GoT";

UPDATE shows SET title = "Grey's Anatomy" WHERE title LIKE "Grey%";

UPDATE shows SET title = "It's Always Sunny in Philidelphia" WHERE title LIKE "%Philidelphia";

UPDATE shows SET title = "Parks and Recreation" WHERE title LIKE "Parks and Rec";

UPDATE shows SET title = "The Office" WHERE title LIKE "Office";




SELECT * FROM shows ORDER BY title;
