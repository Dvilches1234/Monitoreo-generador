from app import app
from datetime import datetime
from flask import render_template
from flask import request
from config import *

import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,password))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
    print "Showing index..."
    return render_template("index.html")

# recibe post desde el lado del cliente
@app.route('/data', methods=['POST'])
def post():
    i = request.form['i']
    v = request.form['v']
    fecha = datetime.now()
    sql = """
    insert into meditions (intensidad, velViento, fecha) values ((%s), (%s), ('%s'));
    """%(i,v,fecha)
    print "Saving the next values: ",i,v,fecha
    cur.execute(sql)
    conn.commit()
    return "200" #return ok

@app.route('/charts')
def charts():
    print "Showing charts..."
    sql="""
    select intensidad, velViento from Meditions;
    """
    cur.execute(sql)
    row = cur.fetchall()
    row.sort()
    intensidad = []
    velViento = []
    for item in row:
        intensidad.append(item[0])
        velViento.append(item[1])

    return render_template("charts.html", intensidad = intensidad, velViento = velViento)
