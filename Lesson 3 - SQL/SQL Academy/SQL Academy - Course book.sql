/* Возвращают строку, которой все символы записаны в нижнем регистре */
SELECT LOWER('SQL Academy') AS lower_string;


/* Возвращает год для даты */
SELECT YEAR('2023-03-13') AS year;


/* Возвращает позицию первого вхождения подстроки в строку */
SELECT INSTR('sql-academy', 'academy') AS idx;


/* Так нижележащий запрос высчитывает длину полного имени для каждого из членов семьи. */
SELECT member_name, LENGTH(member_name) AS name_length
FROM FamilyMembers;


/* Задача 1:
Так нижележащий запрос высчитывает длину полного имени для каждого из 
членов семьи. Так нижележащий запрос высчитывает длину полного имени для
каждого из членов семьи. */
SELECT LOWER('Hello world') AS lower_string;


/* Задача 2:
Выведите полное имя члена семьи и его год рождения.
Для вывода года рождения используйте псевдоним year_of_birth. */
SELECT member_name, YEAR(birthday) AS year_of_birth
FROM FamilyMembers;


/* Задача 3:
Выведите полное имя члена семьи и длину его фамилии.
Для вывода длины фамилии используйте псевдоним lastname_length. */
SELECT member_name,
LENGTH(SUBSTRING_INDEX(member_name,' ', -1)) AS lastname_length
FROM FamilyMembers;
/* ссылка на функцию SUBSTRING_INDEX()
https://www.w3schools.com/sql/func_mysql_substring_index.asp */


/* Задача 4:
Выведите только уникальные имена first_name студентов из таблицы Student. */
SELECT DISTINCT first_name FROM Student;


/* Задача 5:
Выведите только уникальные пары значений идентификатор учителя teacher
и идентификатор предмета subject из таблицы Schedule. */
SELECT DISTINCT teacher, subject FROM Schedule;


SELECT * FROM Student
WHERE first_name = 'Grigoriy' AND YEAR(birthday) > 2000;


/* Давайте для примера выведем все полёты, которые были совершены
на самолёте «Boeing», но, при этом, вылет был не из Лондона: */
SELECT * FROM Trip
WHERE plane = 'Boeing' AND NOT town_from = 'London';


/* Задача 6:
Выведите идентификаторы товаров (поле good) из таблицы Payments,
стоимость которых больше 2000 единиц. Стоимость товара хранится в поле unit_price. */
SELECT good FROM Payments
WHERE unit_price > 2000;


/* Задача 7:
Выведите имена (поле member_name) членов семьи из
таблицы FamilyMembers, чей статус (поле status) равен "father". */
SELECT member_name FROM FamilyMembers
WHERE status = 'father';  /* WHERE status LIKE 'father'


/* Задача 8:
Выведите имя (поле member_name) и дату рождения (поле birthday) членов семьи из таблицы FamilyMembers,
чей статус (поле status) равен "father" или "mother". */
SELECT member_name, birthday
FROM FamilyMembers
WHERE status IN ('father', 'mother');


/* Задача 9:
Необходимо получить все комнаты, в которых есть как кухня 
(поле has_kitchen), так и интернет (поле has_internet). 
Напишите запрос, удовлетворяющий вышеописанному условию, 
который выводит все поля из таблицы Rooms.
Наличие обозначается 1 или true, а отсутствие 0 или false. */
SELECT * FROM Rooms
WHERE has_kintchen = 1 AND has_internet = 1;


/* Выведем всех преподавателей, у кого отсутствует отчество: */
SELECT * FROM Teacher
WHERE middle_name IS NULL;


/* Для использования отрицания, то есть, если мы хотим найти все записи, 
где поле не равно NULL, мы должны использовать следующий синтаксис: */
SELECT * FROM Teacher
WHERE middle_name IS NOT NULL;


/* В качестве результата вернутся все записи из таблицы Payments, 
где значение поля unit_price будет от 100 до 500. */
SELECT * FROM Payments
WHERE unit_price BETWEEN 100 AND 500;


/* Задача 10:
Выведите имена first_name и фамилии last_name 
студентов из таблицы Student, у кого отсутствует отчество middle_name */
SELECT first_name, last_name
FROM Student
WHERE middle_name = NULL;


/* Задача 11:
Выведите резервации комнат (поля room_id, start_date, end_date) из таблицы Reservations, 
у которых итоговая стоимость аренды (поле total) находится в промежутке от 500 до 1200 включительно. */
SELECT room_id, start_date, end_date
FROM Reservations
WHERE total BETWEEN 500 AND 1200;


/* Задача 12:
Выведите информацию о студентах из таблицы Student, 
у которых год рождения соответствует одном из перечисленных: 2000, 2002 и 2004. */
SELECT * FROM Student
WHERE YEAR(birthday) IN (2000, 2002, 2004);


/* Так наш запрос на поиск пользователей в домене «hotmail» может выглядеть следующим образом: */
SELECT name, email
FROM Users
WHERE email LIKE '%@hitmail.%';


/* Например, вы хотите получить идентификаторы задач, прогресс которых равен 3%: */
SELECT job_id FROM Jobs
WHERE progress LIKE '3!%' ESCAPE '!';


/* Задача 13:
Выведите имена всех членов семьи с фамилией "Quincey". */
SELECT member_name FROM FamilyMembers
WHERE member_name LIKE '%Quincey';


/* Выведем информацию о полётах, отсортированную по городу вылета самолёта в порядке возрастания 
и по городу прибытия в аэропорт в порядке убывания, из таблицы Trip: */
SELECT DISTINCT town_from, town_to
FROM Trip
ORDER BY town_from, town_to DESC;


/* Задача 14:
Для каждого отдельного платежа выведите идентификатор товара и сумму, 
потраченную на него, в отсортированном по убыванию этой суммы виде. 
Список платежей находится в таблице Payments.
Для вывода суммы используйте псевдоним sum. */
SELECT good, amount * unit_price AS sum
FROM Payments
ORDER BY sum DESC;


/* Задача 15:
Выведите список членов семьи с фамилией Quincey, 
в отсортированном по возрастанию столбцам status и member_name виде. */
SELECT * FROM FamilyMembers
WHERE member_name LIKE '%Quincey'
ORDER BY status, member_name;


SELECT home_type, AVG(price) as avg_price
FROM Rooms
GROUP BY home_type;


SELECT home_type, AVG(price) as avg_price
FROM Rooms
GROUP BY home_type;


/* Найдём количество каждого вида жилья и отсортируем полученный список по убыванию */
SELECT home_type, COUNT(*) as amount
FROM Rooms
GROUP BY home_type
ORDER BY amount DESC;


/* Для каждого жилого помещения найдём самую позднюю дату выезда (поле end_date) */
SELECT room_id, MAX(end_date) AS last_end_date
FROM Reservations
GROUP BY room_id;


/* Задача 16:
Подсчитайте количество учеников в каждом классе, а также отсортируйте их по убыванию 
количества учеников. Принадлежность ученика к конкретному классу вы 
можете получить из таблицы Student_in_class. 
В качестве результата необходимо вывести идентификатор класса 
(поле class) и количество учеников в этом классе. */
SELECT class, COUNT(*) AS count
FROM Student_in_class
GROUP BY class
ORDER BY count DESC;


/* Задача 17:
Для каждого из существующих статусов (поле status) найдите самого старого человека
(используйте поле birthday). Выведите статус и дату рождения.
Для вывода даты рождения используйте псевдоним birthday. */
SELECT status, MIN(birthday) AS birthday
FROM FamilyMembers
GROUP BY status;


/* Задача 18:
Получите среднее время полётов, совершённых на каждой из моделей самолёта. 
Выведите поле plane и среднее время полёта в секундах.
Для вывода времени используйте псевдоним time.
Используйте функцию TIMESTAMPDIFF(second, time_out, time_in), 
чтобы получить разницу во времени в секундах между двумя датами. */
SELECT plane, AVG(TIMESTAMPDIFF(second, time_out, time_in)) AS time
FROM Trip
GROUP BY plane;
/* http://kodesource.top/mysql/date-and-time-functions/mysql-timestampdiff-function.php */


/* Задача 19:
Выведите идентификатор комнаты (поле room_id), среднюю стоимость 
за один день аренды (поле price, для вывода используйте псевдоним 
avg_price), а также количество резерваций этой комнаты 
(используйте псевдоним count). Полученный результат отсортируйте 
в порядке убывания сначала по количеству резерваций, а потом 
по средней стоимости. */
SELECT room_id, AVG(price) AS avg_price, COUNT(room_id) AS count
FROM Reservations
GROUP BY room_id
ORDER BY count DESC, avg_price DESC;


SELECT home_type, MIN(price) AS min_price FROM Rooms
WHERE has_tv = True
GROUP BY home_type
HAVING COUNT(*) >= 5;


/* Задача 20:
Выведите типы комнат (поле home_type) и разницу между самым дорогим и 
самым дешевым представителем данного типа. В итоговую выборку включите 
только те типы жилья, количество которых в таблице Rooms больше или равно 2.
Для вывода разницы стоимости используйте псевдоним difference. */
SELECT home_type, MAX(price) - MIN(price) AS difference
FROM Rooms
GROUP BY home_type
HAVING COUNT(home_type) >= 2;


/* Задача 21:
Объедините таблицы Class и Student_in_class с помощью внутреннего соединения по полям Class.id и Student_in_class.class. 
Выведите название класса (поле Class.name) и идентификатор ученика (поле Student_in_class.student). */
SELECT
    Class.name,
    Student_in_class.student
FROM
    Class
    INNER JOIN Student_in_class ON
        Class.id = Student_in_class.class;


/* Задача 22:
Дополните запрос из предыдущего задания, добавив ещё одно внутреннее соединение с таблицей Student. 
Объедините по полям Student_in_class.student и Student.id и вместо идентификатора ученика выведите его имя (поле first_name). */
SELECT
    Class.name,
    Student.first_name
FROM
    Student_in_class
    INNER JOIN Class ON
        Student_in_class.class = Class.id
    INNER JOIN Student ON
        Student_in_class.student = Student.id;


/* Задача 23:
Выведите названия продуктов, которые покупал член семьи со статусом "son". 
Для получения выборки вам нужно объединить таблицу Payments с таблицей FamilyMembers по полям family_member и member_id, 
а также с таблицей Goods по полям good и good_id. */
SELECT 
    Goods.good_name 
FROM
    Goods
    INNER JOIN Payments ON
        Goods.good_id = Payments.good
    INNER JOIN FamilyMembers ON 
        Payments.family_member = FamilyMembers.member_id
WHERE
    FamilyMembers.status = 'son';


/* Задача 24:
Выведите идентификатор (поле room_id) и среднюю оценку комнаты (поле rating, для вывода используйте псевдоним avg_score), 
составленную на основании отзывов из таблицы Reviews.
Данная таблица связана с Reservations (таблица, где вы можете взять идентификатор комнаты) по полям reservation_id и Reservations.id. */
SELECT 
    Reservations.room_id, 
    AVG(Reviews.rating) AS avg_score
FROM 
    Reviews
    INNER JOIN Reservations ON 
        Reviews.reservation_id = Reservations.id
GROUP BY
    Reservations.room_id;
    