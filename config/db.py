from sqlalchemy import create_engine, MetaData

# engine=create_engine("mysql:pymysql://root:''@localhost:3306/bdtareas")
engine = create_engine("mysql://memo:root@localhost/bdtareas")
meta=MetaData()
con=engine.connect()