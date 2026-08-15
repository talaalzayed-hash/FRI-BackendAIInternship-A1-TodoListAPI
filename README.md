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

<img width="458" height="51" alt="image" src="https://github.com/user-attachments/assets/f9aa57cc-5267-486f-8b50-8cdb415e14ee" />

<img width="1425" height="805" alt="1 Get-root" src="https://github.com/user-attachments/assets/4a646316-e8a2-4c46-b93b-c3c5f4beb87b" />

### GET `/health` — Health check
GET health returning 200 with status ok

<img width="506" height="52" alt="Screenshot 2026-08-15 170036" src="https://github.com/user-attachments/assets/88f12e7a-c696-4de6-b4ac-aaa9d43b3bc4" />

<img width="1431" height="756" alt="2 health test" src="https://github.com/user-attachments/assets/ca364187-e2ee-4a1b-8502-f7b24cc3bb09" />

### GET `/tasks` — Get all tasks
GET tasks returning 200 with the list of seeded tasks

<img width="382" height="74" alt="Screenshot 2026-08-15 165649" src="https://github.com/user-attachments/assets/c0ade29d-f9fe-4763-9f89-7f106c5e8e2c" />

<img width="1436" height="911" alt="3 get-all-tasks" src="https://github.com/user-attachments/assets/bc317c91-4d3a-4fc2-ab34-e5ca5c2ac2fc" />

### GET `/tasks/{id}` -- Get Task by id 

<img width="748" height="40" alt="Screenshot 2026-08-15 170352" src="https://github.com/user-attachments/assets/eef56632-53c0-40bb-9891-0386953adc74" />

<img width="1150" height="768" alt="Screenshot 2026-08-15 170640" src="https://github.com/user-attachments/assets/b7e44de0-8ae9-4a73-bbf9-3327a9038177" />

### GET `/tasks/{id}` — Task not found
Requesting an ID that does not exist returns 404.

<img width="764" height="28" alt="Screenshot 2026-08-15 170558" src="https://github.com/user-attachments/assets/444e061e-d238-439d-9ad6-ca90164a780c" />

<img width="1423" height="770" alt="Screenshot 2026-08-15 150850" src="https://github.com/user-attachments/assets/98b679a4-2c18-40ee-9804-22ab5d0ebd0d" />

### POST `/tasks` — Create a task

POST tasks returning 201 with the newly created task

<img width="1433" height="893" alt="5 Post" src="https://github.com/user-attachments/assets/598af295-081a-4962-9a25-48e9d0d634a3" />

### POST `/tasks` — Empty title

An empty `title` is rejected with 400.

<img width="1277" height="846" alt="5 POST-title required" src="https://github.com/user-attachments/assets/c4831f0a-e48f-41ac-93b5-338c4bb28ddf" />


### PUT `/tasks/{id}` — Update a task

PUT tasks/1 returning 201 with the updated task

<img width="1145" height="915" alt="6 put" src="https://github.com/user-attachments/assets/93042bd6-b8b2-4d55-b736-6176b51d452b" />

### PUT `/tasks/{id}` — Empty title

PUT tasks/1 with an empty title returning 400 Title is required

<img width="1148" height="881" alt="6 put-title" src="https://github.com/user-attachments/assets/bcc02445-3898-497b-b389-f24354a8ae8f" />


### DELETE `/tasks/{id}` — Delete a task

DELETE tasks/1 returning 204 with no content

<img width="546" height="41" alt="Screenshot 2026-08-15 171755" src="https://github.com/user-attachments/assets/f9673b27-5edf-498c-bb0b-d81371fb4fb8" />

<img width="1154" height="666" alt="7 delete" src="https://github.com/user-attachments/assets/65bc3fc6-d2d6-4309-b2f8-677a7eb0d70f" />

### DELETE `/tasks/{id}` — Task not found

Deleting the same task again returns 404.

<img width="546" height="41" alt="Screenshot 2026-08-15 171755" src="https://github.com/user-attachments/assets/f9673b27-5edf-498c-bb0b-d81371fb4fb8" />

<img width="1144" height="769" alt="7 delete-404" src="https://github.com/user-attachments/assets/42ba8d9f-e894-4d02-ad38-6d277b07c189" />



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
