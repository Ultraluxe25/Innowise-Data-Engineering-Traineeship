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
SELECT
	actor.actor_id,
	actor.first_name,
	actor.last_name,
	COUNT(rental.rental_id) AS rented_times
FROM
	actor
	LEFT JOIN film_actor ON
		actor.actor_id = film_actor.actor_id
	LEFT JOIN film ON
		film_actor.film_id = film.film_id
	LEFT JOIN inventory ON
		film.film_id = inventory.film_id
	LEFT JOIN rental ON
		inventory.inventory_id = rental.inventory_id
GROUP BY
	actor.actor_id
ORDER BY
	rented_times DESC
LIMIT
	10;
