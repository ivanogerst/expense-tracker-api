from fastapi import FastAPI

from database import Base, engine
from routers import expenses, users, auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(expenses.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Expense tracker is running"}