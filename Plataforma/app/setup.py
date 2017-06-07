from config import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,password))

cur = conn.cursor()
sql ="""select 'drop table "' || tablename || '" cascade;' from pg_tables;""" #
cur.execute(sql)

sql = """
CREATE TABLE Meditions(id serial PRIMARY KEY, intensidad decimal, velViento decimal, Fecha timestamp);
"""
#queda con 255 el varchar
cur.execute(sql)
conn.commit()
cur.close()
conn.close()
