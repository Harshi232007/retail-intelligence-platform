from fastapi import FastAPI
import sqlite3

app = FastAPI()

def get_connection():
    conn = sqlite3.connect("../database/retail.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def home():
    return {
        "message": "Retail Intelligence Platform API"
    }
@app.get("/total_sales")
def total_sales():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(Sales)
        FROM sales
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return {
        "Total Sales": total
    }
@app.get("/total_profit")
def total_profit():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(Profit)
        FROM sales
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return {
        "Total Profit": total
    }
@app.get("/categories")
def categories():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT Category
        FROM sales
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
@app.get("/sales_by_category")
def sales_by_category():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT Category,
               SUM(Sales) AS Total_Sales
        FROM sales
        GROUP BY Category
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
@app.get("/profit_by_category")
def profit_by_category():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT Category,
               SUM(Profit) AS Total_Profit
        FROM sales
        GROUP BY Category
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
@app.get("/sales_by_region")
def sales_by_region():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT Region,
               SUM(Sales) AS Total_Sales
        FROM sales
        GROUP BY Region
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
@app.get("/top_products")
def top_products():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT Product_Name,
               SUM(Sales) AS Sales
        FROM sales
        GROUP BY Product_Name
        ORDER BY Sales DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
@app.get("/total_orders")
def total_orders():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM sales
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return {
        "Total Orders": total
    }