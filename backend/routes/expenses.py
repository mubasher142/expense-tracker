from fastapi import APIRouter
from models import Expense
from database import cursor, conn

router = APIRouter()

@router.post("/add-expense")
def add_expense(expense: Expense):
    cursor.execute(
        "INSERT INTO expenses (title, amount) VALUES (?, ?)",
        (expense.title, expense.amount)
    )
    conn.commit()
    return {"message": "Expense added successfully"}

@router.get("/expenses")
def get_expenses():
    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()
    return {"expenses": data}