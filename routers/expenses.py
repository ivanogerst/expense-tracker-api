from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Expense
from schemas import ExpenseCreate, ExpenseResponse

router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.post("/", response_model=ExpenseResponse)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = Expense(**expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@router.get("/{expense_id}", response_model=ExpenseResponse)
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found.")
    return db_expense

@router.get("/", response_model=list[ExpenseResponse])
def read_all_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).all()

@router.get("/user/{user_id}", response_model=list[ExpenseResponse])
def read_expenses_by_user(user_id: int, db: Session = Depends(get_db)):
    db_expenses = db.query(Expense).filter(Expense.user_id == user_id).all()
    return db_expenses

@router.put("/{expense_id}", response_model=ExpenseResponse)
def update_expense(expense_id: int, expense: ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found.")
    db_expense.title = expense.title
    db_expense.amount = expense.amount
    db.commit()
    db.refresh(db_expense)
    return db_expense

@router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found.")
    db.delete(db_expense)
    db.commit()
    return {"message": "Expense successfully deleted."}