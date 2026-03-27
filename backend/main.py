from fastapi import FastAPI
from routes.expenses import router as expense_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Expense Tracker API running 🚀"}

app.include_router(expense_router)

