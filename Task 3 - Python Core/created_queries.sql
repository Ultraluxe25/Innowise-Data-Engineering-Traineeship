-- 1. List of rooms and number of students in each room
SELECT
	rooms.name AS room_number,
	COUNT(students.id) AS residents
FROM
	rooms
	INNER JOIN students ON
		rooms.id = students.room
GROUP BY
	rooms.name;


-- 2. 5 rooms with the smallest average student age
SELECT
    rooms.name,
    AVG(
        AGE(CURRENT_DATE, students.birthday)
    ) AS average_age
FROM
	rooms
	INNER JOIN students ON
		rooms.id = students.room
GROUP BY
	rooms.name
ORDER BY
    average_age ASC
LIMIT
    5;


-- 3. 5 rooms with the biggest difference in student age
SELECT
    rooms.name,
    MAX(AGE(CURRENT_DATE, students.birthday)) - MIN(AGE(CURRENT_DATE, students.birthday)) 
		AS age_difference
FROM
	rooms
	INNER JOIN students ON
		rooms.id = students.room
GROUP BY
	rooms.name
ORDER BY
    age_difference DESC
LIMIT
    5;


-- 4. List of rooms where both boys and girls have been living
SELECT
	rooms.name AS room_number		
FROM
	rooms
	INNER JOIN students ON
		rooms.id = students.room
GROUP BY
	rooms.name
HAVING
	COUNT(DISTINCT students.sex) = 2;
