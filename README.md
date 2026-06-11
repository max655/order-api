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
