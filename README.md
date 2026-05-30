# Expense Tracker API
 
A simple REST API for managing personal expenses, built with FastAPI, SQLAlchemy, and PostgreSQL.
 
## Tech Stack
 
- **FastAPI** – web framework
- **SQLAlchemy** – ORM
- **PostgreSQL** – database
- **Pydantic** – data validation
## Project Structure
 
```
expense-tracker/
├── main.py         # API routes
├── database.py     # DB connection and session
├── models.py       # SQLAlchemy models
├── schemas.py      # Pydantic schemas
└── requirements.txt
```


----------------------------------------------------

## Setup
 
**1. Clone the repo and install dependencies**
```bash
pip install -r requirements.txt
```
 
**2. Create a PostgreSQL database**
```sql
CREATE DATABASE expense_tracker;
```
 
**3. Update the database URL in `database.py`**
```python
DATABASE_URL = "postgresql://your_user:your_password@localhost:5432/expense_tracker"
```
 
**4. Run the server**
```bash
uvicorn main:app --reload
```
 
The API will be available at `http://localhost:8000`.  
Interactive docs at `http://localhost:8000/docs`.
