-- 1. Display the number of films in each category, sorted in descending order.
SELECT
	COUNT(film_category.film_id) AS films_in_category,
	category.category_id
FROM
	category
    LEFT JOIN film_category ON
		category.category_id = film_category.category_id
GROUP BY
	category.category_id
ORDER BY
	films_in_category DESC;


-- 2. Display the 10 actors whose films rented the most, sorted in descending order.
