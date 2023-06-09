import json
from fastapi import APIRouter
from sqlalchemy import Table, select
from config.db import con, meta, engine
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
    
    query = select(Table('tareas', meta, autoload=True, autoload_with=engine))
    res_proxy = con.execute(query)
    res = res_proxy.fetchall()
    results = [tuple(row) for row in res]    
    json_object = json.dumps(results)
    
    return json_object
    # return con.execute(tareas.select().fetch_all())
    
@tarea.get('/')
def get_tareas():
    return tareas