query1 = '''
    SELECT
        rooms.name AS room_number,
        COUNT(students.id) AS residents
    FROM
        rooms
        INNER JOIN students ON
            rooms.id = students.room
    GROUP BY
        rooms.name;
    '''

query2 = '''
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
    '''

query3 = '''
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
    '''

query4 = '''
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
    '''
