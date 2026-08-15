from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

tasks = [
    {"id": 1, "title": "Learn FastAPI","done": False},
    {"id": 2, "title": "Build a REST API", "done": True},
    {"id": 3, "title": "Deploy the API", "done": False}
]

class TaskCreate(BaseModel):
    title: str
    done: bool

@app.get("/")
async def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
async def health():
    return {
        "status": "ok"
    }

@app.get("/tasks")
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return JSONResponse(
        status_code=404,
        content={
            "message": f"Task {task_id} not found"
        }
    )

@app.post("/tasks", status_code=201)
async def create_task(task: TaskCreate):
    if not task.title.strip():
        return JSONResponse(
            status_code=400,
            content={
                "message": "Title is required"
            }
        )
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": task.done
    }
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}", status_code=201)
async def update_task(task_id: int, task: TaskCreate):
    if not task.title.strip():
        return JSONResponse(
            status_code=400,
            content={
                "message": "Title is required"
            }
        )
    for existing_task in tasks:
        if existing_task["id"] == task_id:
            existing_task["title"] = task.title
            existing_task["done"] = task.done
            return {
                "task": existing_task
            }
    return JSONResponse(
        status_code=404,
        content={
            "message": f"Task {task_id} not found"
        }
    )

@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return 
    return JSONResponse(
        status_code=404,
        content={
            "message": f"Task {task_id} not found"
        }
    )
