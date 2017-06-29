from config import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,password))

cur = conn.cursor()
sql ="""select 'drop table "' || tablename || '" cascade;' from pg_tables;""" #
cur.execute(sql)

sql = """
DROP TABLE IF EXISTS Meditions;
DROP TABLE IF EXISTS Lugares;
CREATE TABLE Meditions(id serial PRIMARY KEY, intensidad decimal, velViento decimal, fecha timestamp, lugar integer);
CREATE TABLE Lugares(id serial PRIMARY KEY, lugar varchar);
"""

#queda con 255 el varchar
cur.execute(sql)
conn.commit()
cur.close()
conn.close()
