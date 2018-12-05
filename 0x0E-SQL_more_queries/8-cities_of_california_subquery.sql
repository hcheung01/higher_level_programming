-- Lists all the cities of California found in a database
SELECT cities.id, cities.name
FROM hbtn_0d_usa.cities, hbtn_0d_usa.states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id;
