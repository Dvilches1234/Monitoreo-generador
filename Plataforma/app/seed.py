from config import *
from datetime import datetime
import psycopg2

conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,password))
cur = conn.cursor()

fecha = datetime.now()
sql = """
insert into meditions (intensidad, velViento, fecha) values ('0.3','20.5', ('%s'))
returning
intensidad, velViento, fecha;
"""%(fecha)

cur.execute(sql)
conn.commit()
medicion = cur.fetchone()
print(medicion)

conn.close()
