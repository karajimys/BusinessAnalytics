Try some queries in the site below. There are tables of Customers, Orders, and Shipping: 
[https://www.programiz.com/sql/online-compiler/](https://www.programiz.com/sql/online-compiler/)

--Choose all columns from Customers Table
SELECT * FROM Customers;

--Find all countries where customer is 22 years old
SELECT country
FROM Customers
WHERE age==22;

--Find all countries where customer is above 25 years old
SELECT country
FROM Customers
WHERE age>25;

--Find Customers first and last name with order of amount 400
SELECT Customers.first_name, Customers.last_name 
FROM Customers 
INNER JOIN Orders
ON Orders.customer_id = Customers.customer_id
WHERE  Orders.amount==400;