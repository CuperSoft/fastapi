from fastapi import FastAPI
from routes.tareas import tarea
app=FastAPI()
app.include_router(tarea)
