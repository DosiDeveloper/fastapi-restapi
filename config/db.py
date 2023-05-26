from sqlalchemy import create_engine, MetaData

global conn

try: 
  engine = create_engine("mysql+pymysql://root:password@localhost:3306/storedb")
  conn = engine.connect()
except: 
  engine = create_engine("sqlite:///db.sqlite3")
  conn = engine.connect()

meta = MetaData()
