# Todo API with JWT Authentication

A REST API built with Flask and MySQL that allows users to manage their personal todos with JWT authentication.

## Tech Stack
- Python
- Flask
- MySQL
- JWT (PyJWT)
- bcrypt
- Postman

## Project Structure
Todo_api/
├── app.py
├── Config.py
├── database.py
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   └── todo.py

## API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | /register | No | Register new user |
| POST | /login | No | Login and get JWT token |
| GET | /todo | Yes | Get all my todos |
| POST | /add | Yes | Add new todo |
| PUT | /put/todo/<id> | Yes | Update a todo |
| DELETE | /delete/todo/<id> | Yes | Delete a todo |

## How to Run
1. Clone the repo
2. Install dependencies
   pip install flask flask-mysql PyJWT bcrypt mysql-connector-python
3. Create database in MySQL
4. Run the app
   python app.py
5. Test in Postman → http://127.0.0.1:5000