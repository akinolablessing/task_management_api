## Task Management API (Django + DRF + JWT + MySQL)

This is a task management REST API built with Django REST Framework, SimpleJWT, and MySQL.
Each user can register, log in, and manage their own tasks securely.
#### Auth
- `POST /api/token/` with `username` and `password` to get token
- Use Bearer token in Authorization header
##  Base URL

```
http://localhost:8000
```

##  Postman Testing

###  Register a New User

**POST** `http://localhost:8000/api/register/`  
**Body (JSON):**
```json
{
 "username": "chinedu",
 "password": "chi@134"
}
```
#### Response

```json
{
  "message": "User created successfully."
}
```
### Get JWT Tokens
**POST** `http://localhost:8000/api/token/`
**Body (JSON):**
```
{
   "username": "chinedu",
 "password": "chi@134"
}
```
#### Response

```json
{
  
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MTQ3MDk4NSwiaWF0IjoxNzUxMzg0NTg1LCJqdGkiOiI3M2QwNzYxZmY1ODY0ZjNmYTI2Mzg2NTdlMTk3ZDdhNiIsInVzZXJfaWQiOjd9.uvENqjNDK7S4EhfYULImmxy6AY5n9OYMikK9pu1LeJg",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUxMzg0ODg1LCJpYXQiOjE3NTEzODQ1ODUsImp0aSI6ImUyOTc4OTAwZTY2NTQ3M2E5MTc4YWM5NzI1ZTRkZGNkIiwidXNlcl9pZCI6N30.URgcCOvYtNtnlpU7HOzD02yLJDL9x8m5Co8oGgC1Cj0"

}
```
#### Copy the access token from the response.
### Authorization Header
#### For all protected endpoints, add this header in Postman:
#### Authorization: Bearer <access_token>

## Task Endpoints
### Create Task
**POST** `http://localhost:8000/api/tasks/`
**Body (JSON):**

```
{
  "title": "Finish backend",
  "description": "Write Django views and serializers",
  "due_date": "2025-07-10",
  "completed": false,
  "priority": "high"
}

```
### Get Single Task
**GET** `http://localhost:8000/api/tasks/<id>/`

### Update Task
**PUT** `http://localhost:8000/api/tasks/<id>/`
#### Use the same JSON structure as in Create Task.

### Mark as Completed
**PATCH** `http://localhost:8000/api/tasks/<id>/mark_complete/`
#### No body needed.

### Delete Task
**DELETE** `http://localhost:8000/api/tasks/<id>/`




