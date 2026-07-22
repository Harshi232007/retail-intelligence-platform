from fastapi import APIRouter, HTTPException
from .database import get_connection

router = APIRouter()

@router.get("/")
def home():
    return {
        "message": "Retail Intelligence Platform API"
    }
@router.get("/total_sales")
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
@router.get("/total_profit")
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
@router.get("/categories")
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
@router.get("/sales_by_category")
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
@router.get("/profit_by_category")
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
@router.get("/sales_by_region")
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
@router.get("/top_products")
def top_products():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT "Product.Name",
               SUM(Sales) AS Sales
        FROM sales
        GROUP BY "Product.Name"
        ORDER BY Sales DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
@router.get("/total_orders")
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
@router.get("/product/{product_name}")
def get_product(product_name: str):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM sales
        WHERE "Product.Name" LIKE ?
        LIMIT 20
    """, ('%' + product_name + '%',))

    rows = cursor.fetchall()

    conn.close()

    if not rows:
        raise HTTPException(status_code=404,
                            detail="Product not found")

    return [dict(row) for row in rows]
@router.get("/category/{category}")
def category_filter(category: str):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM sales
        WHERE Category = ?
        LIMIT 20
    """, (category,))

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
@router.get("/region/{region}")
def region_filter(region: str):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM sales
        WHERE Region = ?
        LIMIT 20
    """, (region,))

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
@router.get("/state/{state}")
def state_filter(state: str):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM sales
        WHERE State = ?
        LIMIT 20
    """, (state,))

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
@router.get("/customer/{customer}")
def search_customer(customer: str):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM sales
        WHERE "Customer.Name" LIKE ?
        LIMIT 20
    """, ('%' + customer + '%',))

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
@router.get("/products_by_category/{category}")
def products_by_category(category: str):

    conn = get_connection()
    cursor = conn.cursor()

    if category == "All":
        cursor.execute("""
            SELECT "Product.Name", Category, SUM(Sales) AS Sales
            FROM sales
            GROUP BY "Product.Name", Category
            ORDER BY Sales DESC
            LIMIT 20
        """)
    else:
        cursor.execute("""
            SELECT "Product.Name", Category, SUM(Sales) AS Sales
            FROM sales
            WHERE Category = ?
            GROUP BY "Product.Name", Category
            ORDER BY Sales DESC
            LIMIT 20
        """, (category,))

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
@router.get("/top_customers")
def top_customers():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT "Customer.Name",
               SUM(Sales) AS Sales
        FROM sales
        GROUP BY "Customer.Name"
        ORDER BY Sales DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
@router.get("/category_summary")
def category_summary():

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
@router.get("/monthly_sales")
def monthly_sales():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            substr("Order.Date", 6, 2) AS Month,
            SUM(Sales) AS Total_Sales
        FROM sales
        GROUP BY Month
        ORDER BY Month
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]