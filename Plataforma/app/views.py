from app import app
from datetime import datetime
from flask import render_template
from flask import request
from app.config import *
import psycopg2
import time
import serial
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,password))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
    print ("Showing index...")
    return render_template("index.html")

# recibe post desde el lado del cliente
# @app.route('/data', methods=['POST'])
# def post():
#     i = request.form['i']
#     v = request.form['v']
#     l = request.form['l']
#     fecha = datetime.now()
#
#     sql = """
#     SELECT id FROM lugar where lugar = ('%s');
#     """%(l)
#     cur.execute(sql)
#     lugar_id = cur.fetchone()
#     if not lugar_id:
#         print "ERROR THAT PLACE DOESN'T EXIST"
#         # return "404"
#
#     lugar_id = lugar_id[0]
#
#     sql = """
#     insert into meditions (intensidad, velViento, fecha, lugar) values ((%s), (%s), ('%s'), (%s));
#     """%(i,v,fecha,lugar_id)
#     print ("Saving the next values: ",i,v,fecha,lugar_id)
#     cur.execute(sql)
#     conn.commit()
#     return "200" #return ok

@app.route('/charts', methods=['GET'])
def charts():
    lugar = request.args.getlist('lugar')
    print ("Showing charts...")
    if lugar:
        sql="""
        select intensidad, velViento, fecha, lugar.lugar from Meditions, lugar where meditions.lugar='%s'
        and lugar.id=meditions.lugar;
        """%(lugar[0])
    else:
        sql="""
        select intensidad, velViento, fecha from Meditions;
        """

    cur.execute(sql)
    row = cur.fetchall()
    row.sort()
    intensidad = []
    velViento = []
    fecha = []
    if len(row) == 4:
        lugar = row[3]
    else:
        lugar = ""

    for item in row:
        intensidad.append(item[0])
        velViento.append(item[1])
        a=str(item[2].hour)+":"+str(item[2].minute)+":"+str(item[2].second) #TODO: deberia poner fecha
        fecha.append(a)

    return render_template("charts.html", intensidad = intensidad, velViento = velViento, fecha = fecha, lugar=lugar)

@app.route('/measure')
def measuring():
    print("esta measurando")
    return render_template("measure.html")
