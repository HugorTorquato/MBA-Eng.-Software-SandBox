SELECT * FROM sakila.actor ORDER BY actor_id DESC;

SELECT First_name FROM sakila.actor;

-- Exemple with Alias
SELECT *, BANANA.first_name FROM sakila.actor BANANA;


-- Error trying to search for a varchar without ''
-- error SELECT * FROM sakila.actor WHERE first_name = ADAM;
SELECT * FROM sakila.actor WHERE first_name = 'ADAM';

-- More than one condition within the where clause
SELECT * FROM sakila.actor WHERE first_name = 'ADAM' OR last_name = 'GRANT';
SELECT * FROM sakila.actor WHERE first_name = 'ADAM' AND last_name = 'GRANT';

-- Group ele elements. Aggregation functions can be used here as well
SELECT distinct first_name FROM sakila.actor;

-- Aggregation analysis

SELECT * FROM sakila.payment;
SELECT MAX(amount) FROM sakila.payment;
SELECT MIN(amount) FROM sakila.payment;
SELECT SUM(amount) AS SumAmount FROM sakila.payment;
SELECT AVG(amount) AS AvgAmount FROM sakila.payment;
SELECT COUNT(*) FROM sakila.payment;
SELECT COUNT(DISTINCT(amount)) FROM sakila.payment;


SELECT * FROM sakila.film_category;
SELECT category_id, count(film_id) FROM sakila.film_category GROUP BY last_update;



-- Create a table
CREATE TABLE sakila.endereco
(
	Id_Estudante INTEGER,
    Endereco Varchar(50)
)

SELECT * FROM sakila.endereco;

INSERT INTO sakila.endereco (Id_Estudante, Endereco)
VALUES (2, 'Rua Peixoto da silva');

SELECT * FROM sakila.endereco;




