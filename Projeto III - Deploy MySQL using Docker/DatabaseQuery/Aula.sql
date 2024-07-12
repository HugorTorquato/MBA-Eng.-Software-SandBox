select * 
from world_x.country c
left join world_x.city cc
on cc.CountryCode = c.Code;

select * 
from world_x.country c
right join world_x.city cc
on cc.CountryCode = c.Code;

/* */

/* Nested Query - No need but just for the example */
select * from sakila.film
where film_id in 
(
	select film_id from sakila.film
	where film_id >= 10
);

/* Nested Query - No need but just for the example - In case using this in the From, it is required to have an Alias "nastedQuery" in this case */
select * from 
(
	select * from sakila.film
	where film_id >= 10
) as nestedQuery;

/* Union All- One query is a complement from the other - put everything together in the order it appears - Whitou the ALL it applies an DISTINCT to the query */
select * from sakila.film
where film_id >= 10
UNION
select * from sakila.film
where film_id <= 10;

/* JOIN */
select * from sakila.film;
select * from sakila.film_actor;

/* LEFT JOIN - freeze the film and repeat the line for each time it finds a item in the second table film_Actor - It repeates the name of the film for each actor on it*/
select * 
from sakila.film f
left join sakila.film_actor fa
on f.film_id = fa.film_id;

/* Right JOIN - freeze the film_Actor table. It'll repeat 4 times because has 4 actors in there*/
select * 
from sakila.film f
right join sakila.film_actor fa
on f.film_id = fa.film_id;

/* JOIN */
select * from sakila.payment;
select * from sakila.customer;

/* LEFT JOING with nested query in the join - just for example */
select * 
from sakila.payment p
left join 
(
	sakila.customer c
)
on c.customer_id = p.customer_id;

/* LEFT JOIN - Return numm because the first_name is in the referenced table and not th fixed one in the JOIN*/
select c.first_name, sum(p.amount)
from sakila.payment p
left join 
(
	select * from sakila.customer
    where customer_id <> 1
) c
on c.customer_id = p.customer_id
group by c.first_name;















