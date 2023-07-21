-- Add index for the query: List of rooms and number of students in each room
CREATE INDEX idx_rooms_id ON rooms (id);
CREATE INDEX idx_students_room ON students (room);

-- Add index for the query: 5 rooms with the smallest average student age
CREATE INDEX idx_students_birthday ON students (birthday);

-- Add index for the query: 5 rooms with the biggest difference in student age
CREATE INDEX idx_students_birthday_room ON students (room, birthday);

-- Add index for the query: List of rooms where both boys and girls have been living
CREATE INDEX idx_students_sex_room ON students (sex, room);
