from flask import Flask, render_template, request, redirect
from app import *
from config import *

import psycopg2

conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,password))
cur = conn.cursor()

@app.before_request
def before_request():
    pass
@app.route('/')
@app.route('/home', methods=['POST','GET'])
def home():

    sql ="""
	SELECT nombre, apellido FROM doctores WHERE cirujano='0' LIMIT 3;
	"""
    print sql
    cur.execute(sql)
    doctores = cur.fetchall()

    sql ="""
	SELECT nombre, apellido FROM doctores WHERE cirujano='1' LIMIT 3;
	"""
    print sql
    cur.execute(sql)
    cirujanos = cur.fetchall()
    if request.method == 'POST':
        RutDoc = search.data['doctores.rut']
        sql ="""
	    SELECT * FROM doctores, enfermeros, pacientes WHERE doctores.rut = %s;
	    """('%s')
        print sql
        cur.execute(sql)
        resultado = cur.fetchall()
        render_template("home.html")
    return render_template("home.html", doctores=doctores, cirujanos=cirujanos)

@app.route('/anadir_Pac', methods=["POST",'GET'])
def anadir_Pac():
    if request.method == 'POST':
        rut = request.form['rut']
        edad = request.form['edad']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        genero = request.form['genero']
        tratamiento = request.form['tratamiento']
        Tipo_Cons = request.form['Tipo de Consulta']
        sql=""" INSERT INTO paciente (rut, edad, nombre, apellido, genero, tratamiento)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s');"""%(rut, edad, nombre, apellido, genero, tratamiento)
        cur.execute(sql)
        conn.commit()

        return render_template("anadir_Pac.html", rut=rut, edad=edad, nombre=nombre,
        apellido=apellido, genero=genero, tratamiento=tratamiento)
    return render_template("anadir_Pac.html")

@app.route('/asignEnf', methods=['POST','GET'])
def anadirEnf():
    if request.method is 'POST':
        rut = request.form['rut']
        edad = request.form['edad']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        genero = request.form['genero']
        especialidad  = request.form['especialidad']
        Rut_CirDoc = request.form['Rut_CirDoc']

        sql=""" INSERT INTO enfermero (rut, nombre, apellido, edad, genero, espec, Rut_CirDoc)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s');"""%(rut, nombre, apellido , edad, genero, especialidad, Rut_CirEnf)
        cur.execute(sql)
        conn.commit()

        return render_template("asignEnf.html", rut=rut, edad=edad, nombre=nombre, apellido=apellido,
        genero=genero, especialidad =especialidad, Rut_CirEnf=Rut_CirEnf)
    return render_template('asignEnf.html')

@app.route('/asignDoc', methods=['POST','GET'])
def anadirDoc():
    if request.method is 'POST':
        rut     = request.form['rut']
        edad = request.form['edad']
        nombre= request.form['nombre']
        apellido= request.form['apellido']
        genero = request.form['genero']
        Tipo_Cons   = request.form['Tipo_Cons']
        cirujano = request.form['cirujano']
        Nro_salaDoc = request.form['Nro_salaDoc']
        fecha = request.form['fecha']

        sql=""" INSERT INTO doctor (rut, nombre, apellido, edad, genero, Tipo_Cons , cirujano , Nro_salaDoc, fecha)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s');"""%(rut, nombre, apellido, edad, genero, Tipo_Cons , cirujano , Nro_salaDoc, fecha)
        cur.execute(sql)
        conn.commit()

        return render_template("asignDoc.html", rut=rut,edad=edad ,nombre=nombre ,apellido=apellido ,
        Tipo_Cons=Tipo_Cons, Nro_salaDoc=Nro_salaDoc)
    return render_template('asignDoc.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/asignSala', methods=['GET','POST'])
def asignSala():
    if request.method is 'POST':
        Nro_Sala= request.form['Nro_Sala']
        Tipo = request.form['Tipo']
        piso= request.form['piso']
        sql=""" INSERT INTO salas (Nro_Sala, Tipo, piso)
        VALUES (%s, '%s', '%s');"""%(Nro_Sala, Tipo, piso)
        cur.execute(sql)
        conn.commit()
        return render_template("asignSala.html", Nro_Sala= Nro_Sala, Tipo=Tipo, piso= piso)

    return render_template("asignSala.html")

@app.route('/UpdtSala', methods=['GET','POST'])
def UpdtSala():
    if request.method is 'POST':
        Nro_Sala= request.form['Nro_Sala']
        rut=request.form['rut']
        sql=""" UPDATE doctores SET Nro_salaDoc = %s
        where doctores.rut = %s;"""%(Nro_Sala, rut)
        cur.execute(sql)
        conn.commit()
        return render_template("UpdtSala.html", Nro_Sala= Nro_Sala, rut=rut)

    return render_template("UpdtSala.html")

@app.route('/DeletFunc', methods=['GET','POST'])
def borrarFunc():
    if request.method is 'POST':
        rut= request.method['rut']
        sql="""
        delete from doctores,enfermeros where rut = %s
        ;"""%(rut)
        cur.execute(sql)
        conn.commit()
        return render_template('DeletFunc.html', rut=rut)

    return render_template('DeletFunc.html')

@app.route('/DeletSala', methods =['GET','POST'])
def borrarSala():
    if request.method is 'POST':
        Nro_Sala= request.form['Nro_Sala']
        sql="""
        delete from sala where Nro_sala = %s;
        """%(Nro_sala)
        cur.execute(sql)
        conn.commit()
        return render_template('DeletSala.html' ,Nro_Sala=Nro_Sala)

    return render_template('DeletSala.html')

@app.route('/DeletPac', methods =['GET','POST'])
def borrarPac():
    if request.method is 'POST':
        rut= request.method['rut']
        sql="""
        delete from pacientes where rut = %s;
        """%(rut)
        cur.execute(sql)
        conn.commit()
        return render_template('DeletPac.html' ,rut=rut)

    return render_template('DeletPac.html')
