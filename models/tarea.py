from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta,engine
tareas = Table("tareas", meta, Column("id", Integer),
               Column("descripcion", String(100)))
meta.create_all(engine)
