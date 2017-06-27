from config import *
from datetime import datetime
import psycopg2

conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,password))
cur = conn.cursor()

fecha = datetime.now()
sql = """
insert into meditions (id, intensidad, velViento, fecha, lugar) values ('1','0.3','20.5',('%s'),'1')
returning
id, intensidad, velViento, fecha, lugar;
insert into Lugares(id, lugar) values ('1', 'Home')
returning
id, lugar
"""%(fecha)

cur.execute(sql)
conn.commit()
medicion = cur.fetchone()
print(medicion)

conn.close()
