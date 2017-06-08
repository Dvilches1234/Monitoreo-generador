from app.config import *
from datetime import datetime
import time
import serial
import psycopg2

conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,password))
cur = conn.cursor()

ser = serial.Serial('/dev/ttyACM1', 9600)
while True:
    time.sleep(3)
    date = datetime.now()
    print(date)
    line1 = ser.readline()
    line1 = line1.decode("utf-8")
    line2 = ser.readline()
    line2 = line2.decode("utf-8")
    print("l1",line1)
    print("l2",line2)
    line1 = line1.split(" ")
    line2 = line2.split(" ")
    intensity = 0
    speed = 0
    if line2[0] == "i" :
        intensity = float(line2[1])
    if line1[0] == "v":
        speed = float(line1[1])
    if line1[0] == "i" :
        intensity = float(line1[1])
    if line2[0] == "v":
        speed = float(line2[1])

    print("intensity", intensity)
    print("speed", speed)

    sql = """
    insert into meditions (intensidad, velViento, fecha) values ((%s), (%s), ('%s'));
    """%(intensity, speed, date)
    cur.execute(sql)
    conn.commit()
