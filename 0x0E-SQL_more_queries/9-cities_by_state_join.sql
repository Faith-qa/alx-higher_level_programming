-- lists all cities
-- each record displays cities.id-cities.name-states.name
-- results are sorted in ascending order
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id;
