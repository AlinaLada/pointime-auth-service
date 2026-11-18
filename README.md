# Pointime Auth Service

Authentication and Authorization Microservice for the Pointime platform.

## Project Description

Pointime is an intelligent time management platform that helps users organize schedules, manage tasks, analyze workload, track goals and habits, and coordinate activities with other users.

This repository contains the Authentication and Authorization Service responsible for user management and access control.

## Current Functionality

### User Management

- User registration
- User data storage in PostgreSQL
- Password hashing using bcrypt
- Duplicate email validation

### Authentication

- Secure password hashing
- Authentication service architecture
- REST API endpoints

### Database

- PostgreSQL integration
- Users table
- UUID-based user identification

### API Documentation

- FastAPI Swagger UI
- Interactive API testing

## Technology Stack

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- bcrypt
- Passlib
- Uvicorn
- Pydantic

## Project Structure

auth-service
│
├── app
│ ├── auth.py
│ ├── database.py
│ ├── main.py
│ ├── models.py
│ ├── routes.py
│ ├── schemas.py
│ └── test_db.py
│
├── requirements.txt
├── .gitignore
└── README.md

## Implemented Features

- [x] User Registration
- [x] Password Hashing
- [x] PostgreSQL Connection
- [x] SQLAlchemy Integration
- [x] FastAPI Setup
- [x] Swagger Documentation

## Planned Features

- [ ] User Login
- [ ] JWT Authentication
- [ ] User Logout
- [ ] User Profile Management
- [ ] RabbitMQ Integration
- [ ] Docker Deployment
- [ ] Grafana Monitoring

## Running the Application

Install dependencies:

pip install -r requirements.txt

Run the application:

uvicorn app.main:app --reload

API Documentation:

http://127.0.0.1:8000/docs

## Author

Pointime Project
Authentication Service