1 SELECT State,
       SUM(Sales) AS Total_Sales
FROM sales
GROUP BY State
ORDER BY Total_Sales DESC;
2.SELECT State,
       SUM(Profit) AS Total_Profit
FROM sales
GROUP BY State
ORDER BY Total_Profit DESC;
3.SELECT Category,
       AVG(Discount) AS Average_Discount
FROM sales
GROUP BY Category;
4.SELECT State,
       SUM(Profit) AS Total_Profit
FROM sales
GROUP BY State
ORDER BY Total_Profit DESC
LIMIT 5;
5.SELECT State,
       SUM(Profit) AS Total_Profit
FROM sales
GROUP BY State
ORDER BY Total_Profit ASC
LIMIT 5;
6.SELECT "Ship.Mode",
       COUNT(*) AS Total_Orders
FROM sales
GROUP BY "Ship.Mode";
7.SELECT Segment,
       SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Segment
ORDER BY Total_Sales DESC;
8.SELECT Segment,
       SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Segment
ORDER BY Total_Profit DESC;
9.SELECT "Customer.Name",
       SUM(Sales) AS Total_Sales
FROM sales
GROUP BY "Customer.Name"
HAVING SUM(Sales) > 10000
ORDER BY Total_Sales DESC;
