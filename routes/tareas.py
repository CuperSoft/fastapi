from fastapi import APIRouter
from config.db import con
from models.tarea import tareas
tarea=APIRouter()

tareas=[
    {
        "titulo":"Tender cama",
        "status":"Finalizado"
    }
]
@tarea.get('/tareas')
def read_root():
    return con.execute(tareas.select().fetch_all())
@tarea.get('/')
def get_tareas():
    return tareas