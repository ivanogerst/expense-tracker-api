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
├── main.py
├── database.py
├── models.py
├── schemas.py
├── routers/
│ ├── users.py
│ ├── expenses.py
│ └── auth.py
├── requirements.txt
└── .gitignore
```

## API Endpoints

### Expenses
- POST /expenses/
- GET /expenses/
- GET /expenses/{id}
- PUT /expenses/{id}
- DELETE /expenses/{id}

### Users
- POST /users/
- GET /users/
- GET /users/{id}
- PUT /users/{id}
- DELETE /users/{id}

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
