-- lists all the cities of California that is found in the database hbtn_0d_usa
-- database name is passed as argument of the mysql command
SELECT cities.id, name FROM cities WHERE state_id =
(SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
