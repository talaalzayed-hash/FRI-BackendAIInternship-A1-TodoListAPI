# Todo List API

A small REST API for managing tasks, built with **FastAPI**. Tasks are kept in memory, so the list resets every time the server restarts.

## Tech Stack

- Python 3.12
- FastAPI 0.141.1
- Uvicorn 0.52.2
- Pydantic 2.13.4

## Getting Started

Create and activate a virtual environment:

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install fastapi uvicorn
```

Run the server:

```bash
uvicorn app.main:app --reload
```

The API is then available at `http://127.0.0.1:8000`, and the interactive Swagger docs at `http://127.0.0.1:8000/docs`.

## Task Model

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "done": false
}
```

`id` is assigned by the server. Requests that create or update a task send only `title` and `done`.

## Endpoints

| Method | Path              | Description       | Success |
| ------ | ----------------- | ----------------- | ------- |
| GET    | `/`               | API info          | 200     |
| GET    | `/health`         | Health check      | 200     |
| GET    | `/tasks`          | Get all tasks     | 200     |
| GET    | `/tasks/{id}`     | Get a task by ID  | 200     |
| POST   | `/tasks`          | Create a new task | 201     |
| PUT    | `/tasks/{id}`     | Update a task     | 201     |
| DELETE | `/tasks/{id}`     | Delete a task     | 204     |

### Errors

| Status | When                                        | Body                                  |
| ------ | ------------------------------------------- | ------------------------------------- |
| 400    | `title` is empty or whitespace on POST/PUT  | `{"message": "Title is required"}`    |
| 404    | No task with the given ID                   | `{"message": "Task {id} not found"}`  |

---

## Screenshots
All endpoints were tested through the Swagger UI at `/docs`.

### Swagger UI
Swagger UI listing all endpoints

<img width="1497" height="571" alt="Swagger" src="https://github.com/user-attachments/assets/79520409-b9cd-4280-a4c9-2afc2dccfd6d" />

### GET `/` — API info
GET root returning 200 with the API name, version and endpoints

<img width="1425" height="805" alt="1 Get-root" src="https://github.com/user-attachments/assets/4a646316-e8a2-4c46-b93b-c3c5f4beb87b" />

### GET `/health` — Health check
GET health returning 200 with status ok

<img width="1431" height="756" alt="2 health test" src="https://github.com/user-attachments/assets/ca364187-e2ee-4a1b-8502-f7b24cc3bb09" />

### GET `/tasks` — Get all tasks
GET tasks returning 200 with the list of seeded tasks

<img width="1436" height="911" alt="3 get-all-tasks" src="https://github.com/user-attachments/assets/bc317c91-4d3a-4fc2-ab34-e5ca5c2ac2fc" />

### GET `/tasks/{id}` — Task not found
Requesting an ID that does not exist returns 404.

<img width="1423" height="770" alt="Screenshot 2026-08-15 150850" src="https://github.com/user-attachments/assets/98b679a4-2c18-40ee-9804-22ab5d0ebd0d" />

### POST `/tasks` — Create a task
POST tasks returning 201 with the newly created task


### POST `/tasks` — Empty title

An empty `title` is rejected with 400.

![POST tasks with an empty title returning 400 Title is required](screenshots/06-post-task-400.png)

### PUT `/tasks/{id}` — Update a task

![PUT tasks/1 returning 201 with the updated task](screenshots/07-put-task-201.png)

### PUT `/tasks/{id}` — Empty title

![PUT tasks/1 with an empty title returning 400 Title is required](screenshots/08-put-task-400.png)

### DELETE `/tasks/{id}` — Delete a task

![DELETE tasks/1 returning 204 with no content](screenshots/09-delete-task-204.png)

### DELETE `/tasks/{id}` — Task not found

Deleting the same task again returns 404.

![DELETE tasks/1 returning 404 with Task 1 not found](screenshots/10-delete-task-404.png)

## Project Structure

```
todo-list-api/
├── app/
│   ├── __init__.py
│   └── main.py
├── screenshots/
├── venv/
└── README.md
```
