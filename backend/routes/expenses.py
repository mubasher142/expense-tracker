from fastapi import APIRouter
from models import Expense
from database import cursor, conn

router = APIRouter()

@router.post("/add-expense")
def add_expense(expense: Expense):
    cursor.execute(
        "INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
        (expense.title, expense.amount, expense.category, expense.date)
    )
    conn.commit()
    return {"message": "Expense added successfully"}

@router.get("/expenses")
def get_expenses():
    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()

    expenses = []
    for row in data:
        expenses.append({
            "id": row[0],
            "title": row[1],
            "amount": row[2],
            "category": row[3],
            "date": row[4]
        })

    return {"expenses": expenses}