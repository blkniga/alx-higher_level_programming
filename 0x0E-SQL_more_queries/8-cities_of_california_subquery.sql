-- A script that lists all the cities of California that can be found
-- in the database hbtn_0d_usa

SELECT states.id, cities.name
FROM hbtn_0d_usa.states, hbtn_0d_usa.cities
WHERE cities.name = 'California'
ORDER BY cities.id ASC;
