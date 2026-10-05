# Expense Tracker API

REST API for managing users and personal expenses, built with FastAPI and SQLAlchemy. Includes password hashing, automated tests, Docker support, and GitHub Actions CI.

## Tech Stack

* **FastAPI** – web framework
* **SQLAlchemy** – ORM and database interaction
* **SQLite** – database
* **Pydantic** – request/response validation
* **bcrypt** – password hashing
* **pytest** – automated API testing
* **Docker** – containerization
* **GitHub Actions** – continuous integration

## Project Structure

```text
expense-tracker/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── routers/
│   ├── users.py
│   ├── expenses.py
│   └── auth.py
├── tests/
│   ├── conftest.py
│   ├── test_users.py
│   └── test_auth.py
├── Dockerfile
├── requirements.txt
└── .github/
    └── workflows/
        └── tests.yml
```

## API Endpoints

### Expenses

* `POST /expenses/`
* `GET /expenses/`
* `GET /expenses/{id}`
* `GET /expenses/user/{user_id}`
* `PUT /expenses/{id}`
* `DELETE /expenses/{id}`

### Users

* `POST /users/`
* `GET /users/`
* `GET /users/{id}`
* `PUT /users/{id}`
* `DELETE /users/{id}`

### Authentication

* `POST /auth/login`

User passwords are hashed with bcrypt before being stored.

## Testing

The project uses pytest with an isolated in-memory SQLite database for API tests.

The test suite currently covers:

* User creation
* Duplicate username handling
* User retrieval
* Nonexistent user handling
* Successful login
* Incorrect password
* Unknown user login

Run the tests with:

```bash
pytest
```

## Docker

Build the Docker image:

```bash
docker build -t expense-tracker .
```

Run the container:

```bash
docker run -d -p 8000:8000 --name expense-tracker-app expense-tracker
```

The API will then be available at:

```text
http://localhost:8000
```

Interactive API documentation:

```text
http://localhost:8000/docs
```

## Continuous Integration

GitHub Actions automatically runs the test suite on every push and pull request.

The CI workflow:

1. Sets up Python 3.13
2. Installs project dependencies
3. Runs pytest
4. Reports whether the tests passed or failed
