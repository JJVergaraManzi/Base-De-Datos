from flask import Flask, render_template
from proyecto import *

@app.route('/')
@app.route('/index')
def index():

    sql ="""
	select nombre, apellido from doctor, cirujano, enfermero order by apellido ASC
	"""
    print sql
    cur.execute(sql)
    funcionarios = cur.fetchall()

    sql ="""
	select nombre, apellido, rut from paciente order by apellido ASC
	"""
    print sql
    cur.execute(sql)
    paciente = cur.fetchall()

    pacientes = cur.fetchall()
    return render_template("index.html", funcionarios=funcionarios, paciente=paciente)

@app.route('/anadir_Pac', methods=["POST",'GET'])
def anadir_Pac():
    if request.method == 'POST':
        PacRut = request.form['PacRut']
        PacEd = request.form['PacEd']
        PacNom = request.form['PacNom']
        PacAp = request.form['PacAp']
        PacTrat = request.form['PacTrat']
        PacTipCons = request.form['PacTipCons']
        PacDia = request.form['PacDia']
        PacHorInit = request.form['PacHorInit']
        PacHorFin = request.form['PacHorFin']
        sql=""" INSERT INTO paciente (rut, edad , nombre, apellido , tratamiento, Tipo_Cons, dia, horInit, horFin)
        VALUES (%s, %s, '%s', '%s', '%s', '%s','%s','%s','%s');"""%(PacRut, PacEd, PacNom, PacAp ,PacTrat, PacTipCons,PacDia, PacHorInit, PacHorFin)
        cur.execute(sql)
        conn.commit()

        sql = """select paciente.nombre, paciente.apellido, doctor.nombre, doctor.apellido, sala.Nro_sala
        from doctor, paciente where paciente.Rut_Doc = doctor.rut and sala.Nro_sala = doctor.Nro_salaDoc;"""

        return render_template("anadir_Pac.html", PacRut=PacRut, PacEd=PacEd, PacNom=PacNom,
        PacAp=PacAp, PacTrat=PacTrat, PacTipCons=PacTipCons, PacDia=PacDia, PacHorInit=PacHorInit, PacHorFin=PacHorFin)

@app.route('/anadirCir', methods=["POST",'GET'])
def anadirCir():
    if request.method == 'POST':
        CirRut = request.form['CirRut']
        CirEd = request.form['CirEd']
        CirNom = request.form['CirNom']
        CirAp = request.form['CirAp']
        CirEspec = request.form['CirEspec']
        Nro_salaCir = request.form['Nro_salaCir']
        CirDia = request.form['CirDia']
        CirHorInit = request.form['CirHorInit']
        CirHorFin = request.form['CirHorFin']
        sql=""" INSERT INTO cirujano (rut, edad , nombre, apellido , tratamiento, Tipo_Cons, dia, horInit, horFin)
        VALUES (%s, %s, '%s', '%s', '%s', '%s','%s','%s','%s');"""%(CirRut, CirEd, CirNom, CirAp ,CirEspec, Nro_salaCir, CirDia, CirHorInit, CirHorFin)
        cur.execute(sql)
        conn.commit()

        sql = """select paciente.nombre, paciente.apellido, cirujano.nombre, cirujano.apellido, sala.Nro_sala
        from cirujano, paciente where paciente.Rut_Cir = cirujano.rut and sala.Nro_sala = cirujano.Nro_salaCir;"""

        return render_template("anadir_Pac.html", CirRut=CirRut, CirEd=CirEd, CirNom=CirNom,
        CirAp=CirAp, CirTrat=CirTrat, CirTipCons=CirTipCons, CirDia=CirDia, CirHorInit=CirHorInit, CirHorFin=CirHorFin)

@app.route('/anadir_Pac', methods=['POST','GET'])
def anadirEnf():
    if request.method is 'POST':
        EnfRut     = request.form['EnfRut']
        EnfEd      = request.form['EnfEd']
        EnfNom     = request.form['EnfNom']
        EnfAp      = request.form['EnfAp']
        EnfEspec   = request.form['EnfEspec']
        Rut_CirEnf = request.form['Rut_CirEnf']
        sql=""" INSERT INTO enfermero (rut , nombre, apellido , edad, espec, Rut_CirEnf )
        VALUES (%s, %s, '%s', '%s', '%s', '%s','%s','%s','%s');"""%(EnfRut, EnfEd, EnfNom, EnfAp ,EnfEspec, Rut_CirEnf)
        cur.execute(sql)
        conn.commit()

        sql = """select enfermero.nombre, enfermero.apellido, enfermero.nombre, enfermero.apellido, sala.Nro_sala
        from enfermero, enfermero where enfermero.Rut_Enf = enfermero.rut and sala.Nro_sala = enfermero.Nro_salaCir;"""
        render_template("asign_sala.html", EnfRut=EnfRut, EnfEd=EnfEd, EnfNom=EnfNom, EnfAp=EnfAp, EnfEspec =EnfEspec, Rut_CirEnf=Rut_CirEnf)

@app.route('/atenSala', methods=['POST','GET'])
def atenSala():
    if request.method =='POST':
        NroSalaID = request.form['NroSalaID']
        rutdoc = request.form['rutdoc']
        sql ="""INSERT INTO atiende(NroSala_ID , RutDoc_ID )
        VALUES (%s, %s);"""%(NroSalaID, rutdoc)
        cur.execute(sql)
        conn.commit()
        if not NroSalaID or not rutdoc:
            print"usted no ha ingresado los datos!"
            return redirect("/index")
        else:
            sql = """select nombre, apellido, Nro_sala from doctor
            where doctor.rut = atiende.RutDoc_ID and doctor.Nro_sala= atiende.NroSala_ID; """

    render_template("asign_sala.html", rutdoc=rutdoc, NroSalaID=NroSalaID)

@app.route('/borrarFunc/<rut>', methods=['GET','POST'])
def borrarFunc(rut):

    sql="""
    delete from doctor, cirujano, enfermero where rut = %s
    """%(rut)
    print sql
    cur.execute(sql)
    conn.commit()
    return redirect(request.referrer)

@app.route('/borrarSala/<Nro_sala>', methods =['GET','POST'])
def borrarSala(Nro_sala):

    sql="""
    delete from sala where Nro_sala = %s
    """%(Nro_sala)
    print sql
    cur.execute(sql)
    conn.commit()
    return redirect(request.referrer)
