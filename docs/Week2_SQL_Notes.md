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

## day2 queries
1.SELECT SUM(Sales) AS Total_Sales
FROM sales;
2.SELECT SUM(Profit) AS Total_Profit
FROM sales;
3.SELECT AVG(Sales) AS Average_Sales
FROM sales;
4.SELECT MAX(Sales) AS Highest_Sale
FROM sales;
5.SELECT MIN(Profit) AS Lowest_Profit
FROM sales;
6.SELECT Category,SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Category;
7.SELECT Category,SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Category;
8.SELECT Region,SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region;
9.SELECT "Customer.Name",SUM(Sales) AS Total_Sales
FROM sales
GROUP BY "Customer.Name"
ORDER BY Total_Sales DESC
LIMIT 10;
10.SELECT "Product.Name",SUM(Sales) AS Total_Sales
FROM sales
GROUP BY "Product.Name"
ORDER BY Total_Sales DESC
LIMIT 10;
11.SELECT Category,SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Category
HAVING SUM(Sales) > 100000;
12.SELECT Region,COUNT(*) AS Total_Orders
FROM sales
GROUP BY Region;