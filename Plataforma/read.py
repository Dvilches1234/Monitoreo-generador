from app.config import *
from datetime import datetime
import time
import serial
import psycopg2

conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,password))
cur = conn.cursor()

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(3)
while True:
    intensity = 0
    speed = 0
    try:
        date = datetime.now()
        print(date)
        line1 = ser.readline()
        line2 = ser.readline()
        print("l1",line1)
        print("l2",line2)

        line1 = line1.decode("utf-8")
        line2 = line2.decode("utf-8")
        print("l1",line1)
        print("l2",line2)
        line1 = line1.split(" ")
        line2 = line2.split(" ")

        print("l1",line1, len(line1))
        print("l2",line2, len(line2))

        if len(line1) == 2 and len(line2) == 2:
                try:
                    if line2[0] == "i" :
                        intensity = float(line2[1])
                    if line1[0] == "v":
                        speed = float(line1[1])
                    if line1[0] == "i" :
                        intensity = float(line1[1])
                    if line2[0] == "v":
                        speed = float(line2[1])
                except ValueError:
                    pass

    except serial.SerialException:
        pass

    print("intensity", intensity)
    print("speed", speed)

    #sql = """
    #insert into meditions (intensidad, velViento, fecha) values ((%s), (%s), ('%s'));
    #"""%(intensity, speed, date)
    #cur.execute(sql)
    #   conn.commit()
