# Week 2 - SQL Notes

## What is SQL?
SQL (Structured Query Language) is used to store, retrieve, update, and delete data in a database.

## What is a Database?
A database is an organized collection of data.

## What is a Table?
A table stores related data in rows and columns.

## What is a Row?
A row represents one record.

## What is a Column?
A column represents one attribute of the data.

## What is a Primary Key?
A primary key uniquely identifies each row in a table.
## Queries
select * from sales;
SELECT COUNT(*) AS Total_Orders
FROM sales;
SELECT DISTINCT Category
FROM sales;
SELECT "Product.Name",Sales FROM sales ORDER BY Sales DESC;
SELECT * FROM sales LIMIT 5;
PRAGMA table_info(sales);
SELECT "Customer.Name",Sales
FROM sales
ORDER BY Sales DESC;
SELECT *
FROM sales
WHERE Category = 'Technology';
