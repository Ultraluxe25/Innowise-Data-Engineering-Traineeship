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


-- 2. 