-- Lesson 4 (Karpov courses - SQL)

/* Задание 1:

Напишите SQL-запрос к таблице products и выведите всю информацию о товарах, цена которых не превышает 100 рублей. Результат отсортируйте по возрастанию id товара.

Поля в результирующей таблице: product_id, name, price */

SELECT
    product_id,
    name,
    price
FROM
    products
WHERE
    price <= 100
ORDER BY
    product_id;


/* Задание 2:

Отберите пользователей женского пола из таблицы users. Выведите только id этих пользователей. Результат отсортируйте по возрастанию id.

Добавьте в запрос оператор LIMIT и выведите только 1000 первых id из отсортированного списка.

Поле в результирующей таблице: user_id

Пояснение:

Обратите внимание, что в SELECT можно не включать колонку, которая используется для фильтрации в операторе WHERE. Так, например, в этом задании мы не включаем в результат колонку с полом пользователя. */

SELECT
    user_id
FROM
    users
WHERE
    sex = 'female'
ORDER BY
    user_id
LIMIT
    1000;


/* Задание 3:

Отберите из таблицы user_actions все действия пользователей по созданию заказов, которые были совершены ими после полуночи 6 сентября 2022 года. Выведите колонки с id пользователей, id созданных заказов и временем их создания.

Результат должен быть отсортирован по возрастанию id заказа.

Поля в результирующей таблице: user_id, order_id, time

Пояснение:

Обратите внимание, что в таблице user_actions у каждого пользователя могут быть записи не только со временем создания заказа, но и временем его отмены. Нам необходимо получить только записи с созданием заказов. */

SELECT
    user_id,
    order_id,
    time
FROM
    user_actions
WHERE
    time > '2022-09-06'
    AND action = 'create_order'
ORDER BY
    order_id;


/* Задание 4:

Назначьте скидку 20% на все товары из таблицы products и отберите те, цена на которые с учётом скидки превышает 100 рублей. Выведите id товаров, их наименования, прежнюю цену и новую цену с учётом скидки. Колонку со старой ценой назовите old_price, с новой — new_price.

Результат должен быть отсортирован по возрастанию id товара.

Поля в результирующей таблице: product_id, name, old_price, new_price */

SELECT
    product_id,
    name,
    price AS old_price,
    price * 0.8 AS new_price
FROM
    products
WHERE
    price * 0.8 > 100
ORDER BY
    product_id;


/* 