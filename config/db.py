from sqlalchemy import MetaData, create_engine

engine = create_engine("mysql+pymysql://root:root@localhost:3306/dsproblem")

meta = MetaData()

connection = engine.connect()