from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# DB connection
conn = sqlite3.connect("expenses.db", check_same_thread=False)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    amount REAL
)
""")
conn.commit()

# Root API
@app.get("/")
def read_root():
    return {"message": "Expense Tracker API running 🚀"}

# Pydantic model
class Expense(BaseModel):
    title: str
    amount: float

# POST API
@app.post("/add-expense")
def add_expense(expense: Expense):
    cursor.execute(
        "INSERT INTO expenses (title, amount) VALUES (?, ?)",
        (expense.title, expense.amount)
    )
    conn.commit()
    return {"message": "Expense added successfully"}

# GET API
@app.get("/expenses")
def get_expenses():
    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()
    return {"expenses": data}