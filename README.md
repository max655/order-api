# 🛒 Order Management System API

A RESTful API for managing users and orders, built with FastAPI, PostgreSQL, JWT authentication, Docker, and CI/CD.

---

## 🚀 Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Alembic (migrations)
- JWT Authentication
- Passlib (bcrypt hashing)
- Pytest (testing)
- Docker & Docker Compose
- GitHub Actions (CI)

---

## 📌 Features

### 👤 User Management
- User registration
- User login
- JWT token authentication
- Role-based access control:
  - `user`
  - `admin`

### 📦 Order Management
- Create order (authenticated users)
- Get order by ID
- Update order (owner or admin)
- Delete order (admin only)

---

## 🔐 Authentication

This API uses JWT (JSON Web Tokens).

### Example header:
```http
Authorization: Bearer <your_token>

## ⚙️ Getting Started

1. Clone repository
git clone https://github.com/USERNAME/order-api.git
cd order-api
2. Run with Docker (recommended)
docker compose up --build
3. Run locally (without Docker)
Install dependencies:
pip install -r requirements.txt
Start server:
uvicorn main:app --reload

## 🗄️ Database

PostgreSQL is used as the main database.

Tables:
users
orders
🔄 Database Migrations (Alembic)

Create migration:

alembic revision --autogenerate -m "initial migration"

Apply migrations:

alembic upgrade head
🧪 Running Tests
pytest -v
🐳 Docker Compose
services:
  api:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: orders_db
    ports:
      - "5432:5432"

## 🔁 CI/CD Pipeline

This project uses GitHub Actions for Continuous Integration.

On every push or pull request:

- Install dependencies
- Start PostgreSQL service
- Run tests with pytest

## 📡 API Endpoints

### Authentication
- POST /users/register
- POST /users/login

### Orders
- POST /orders
- GET /orders/{id}
- PUT /orders/{id}
- DELETE /orders/{id}
