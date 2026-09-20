# FastAPI Backend Development

A structured roadmap, learning progress tracker, and project collection for mastering backend engineering with Python and FastAPI.

---

## Prerequisites & Python Foundations

- Modern Python syntax & Type hints (`typing`, `Annotated`)
- Data structures (dicts, sets, lists) & Comprehensions
- Functions, `*args`, `**kwargs`, and decorators
- Object-Oriented Programming (Classes, inheritance)
- Concurrency fundamentals (`async` / `await`, event loops)
- Virtual environments (`venv`, `uv`, or `poetry`)
- Environment variable management (`.env`, `python-dotenv`)

---

## FastAPI Core Concepts

- **HTTP & REST Standards:** Status codes, request methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`), headers
- **Routing & Structure:** Path operations, query parameters, path parameters, request bodies
- **Data Validation & Serialization:** Pydantic models, field validation, response models
- **FastAPI Dependency Injection System:** Reusable dependencies, database session injection, sub-dependencies
- **Error Handling:** `HTTPException`, custom exception handlers, validation error interception
- **Middleware & Security:** CORS, request logging middleware, trusted hosts
- **Background Tasks:** Asynchronous background processing natively in FastAPI
- **Automated Documentation:** Swagger UI (`/docs`) and ReDoc (`/redoc`) customization

---

## Database Management & Persistence

- **Relational Databases:** PostgreSQL / MySQL / SQLite
- **SQL & Query Basics:** CRUD queries, joins, constraints, foreign keys, indexing
- **ORMs & Drivers:** SQLAlchemy 2.0 (Async/Sync) or SQLModel
- **Database Migrations:** Alembic (environment setup, generating migrations, upgrading/downgrading schema)
- **Design Patterns:** Repository pattern, unit of work, session management

---

## Authentication & Authorization

- Password hashing (`passlib`, `bcrypt`)
- OAuth2 with Password (and hashing) flow
- JSON Web Tokens (JWT) access & refresh token implementation
- Role-Based Access Control (RBAC) and protected route dependencies

---

## Testing & Code Quality

- Unit & integration testing with `pytest` and `httpx` (`TestClient`)
- Database test isolation (in-memory SQLite or temporary test DB fixtures)
- Code formatting & linting (`ruff`, `black`, `flake8`)

---

## Deployment & Containerization

- Production ASGI servers (`uvicorn`, `gunicorn` with Uvicorn workers)
- Containerization with Docker (multi-stage builds, `.dockerignore`)
- `docker-compose` for local multi-container environments (FastAPI + Database)
- Deployment to cloud platforms (Render, Railway, or VPS)

---

## Learning Projects

- **Task & Note Tracker API:** Core CRUD, Pydantic validation, SQLite/SQLAlchemy
- **User Auth & Role Management Service:** JWT signup/login flow, hashed passwords, RBAC
- **Blog / Social Feed Engine:** Complex relational queries, pagination, filtering, search
- **E-Commerce Backend:** Orders, carts, transaction boundaries, background email notifications
- **Fully Containerized Production API:** Dockerized FastAPI service wired to PostgreSQL with Alembic migrations and test suite