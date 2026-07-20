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