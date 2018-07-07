from config import *
from datetime import datetime
import psycopg2

conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()

sql = """
insert into salas(Nro_sala, Tipo, Piso)
values (201, 'Consulta', 'segundo')
returning
Nro_Sala, Tipo, piso;
"""

cur.execute(sql)
conn.commit()
sala = cur.fetchone()
print ("Insertamos los datos en salas :" )
print(sala)
# Insertar valores a la tabla Salas
sql = """
insert into salas (Nro_Sala, Tipo, piso)
values (303, 'Consulta', 'tercero')
returning
Nro_Sala, Tipo, piso;
"""

cur.execute(sql)
conn.commit()
sala = cur.fetchone()
print ("Insertamos los datos en salas :" )
print(sala)

sql = """
insert into salas (Nro_Sala, Tipo, piso)
values (304, 'Operacion', 'tercero')
returning
Nro_Sala, Tipo, piso;
"""

cur.execute(sql)
conn.commit()
sala = cur.fetchone()
print ("Insertamos los datos en salas :" )
print(sala)

sql = """
insert into salas (Nro_Sala, Tipo, piso)
values (406, 'operacion', 'cuarto')
returning
Nro_Sala, Tipo, piso;
"""

cur.execute(sql)
conn.commit()
sala = cur.fetchone()
print ("Insertamos los datos en salas :" )
print(sala)

sql=""" insert into doctores(rut, nombre, apellido, edad, genero, Tipo_Cons , cirujano , Nro_salaDoc, fecha)
values (12345, 'gonzalo', 'Gonzales', 29, 'hombre','Oftalmologia', '1', 406, '2014-02-06T10:57Z')
returning rut, nombre, apellido, edad, genero, Tipo_Cons , cirujano , Nro_salaDoc, fecha;
"""
cur.execute(sql)
conn.commit()
doctores = cur.fetchone()
print ("Insertamos los datos en doctores :" )
print(doctores)

sql=""" insert into doctores(rut, nombre, apellido, edad, genero, Tipo_Cons , cirujano , Nro_salaDoc, fecha)
values ('4563', 'Tito', 'Pretoriano', '33', 'hombre','Traumatologia', '0', '201', '2018-05-07T16:30Z')
returning rut, nombre, apellido, edad, genero, Tipo_Cons , cirujano , Nro_salaDoc, fecha;
"""
cur.execute(sql)
conn.commit()
doctores = cur.fetchone()
print ("Insertamos los datos en doctores :" )
print(doctores)

sql=""" insert into doctores(rut, nombre, apellido, edad, genero, Tipo_Cons , cirujano , Nro_salaDoc, fecha)
values ('98760', 'Fernando', 'Fernandez', '33', 'hombre', 'Pediatra', '0', '303', '2018-06-07T17:30Z')
returning rut, nombre, apellido, edad, genero, Tipo_Cons , cirujano , Nro_salaDoc, fecha;
"""
cur.execute(sql)
conn.commit()
doctores = cur.fetchone()
print ("Insertamos los datos en doctores :" )
print(doctores)

sql=""" insert into doctores(rut, nombre, apellido, edad, genero, Tipo_Cons , cirujano , Nro_salaDoc, fecha)
values ('567304', 'Jon', 'Jonson', '32', 'hombre', 'Otorrino', '1', '304', '2018-06-08T18:30Z')
returning rut, nombre, apellido, edad, genero, Tipo_Cons , cirujano , Nro_salaDoc, fecha
"""
cur.execute(sql)
conn.commit()
doctores = cur.fetchone()
print ("Insertamos los datos en doctores :" )
print(doctores)

sql=""" insert into pacientes(rut, edad, nombre, apellido, genero , tratamiento, Rut_Doc)
values ('56784','32', 'Pedro', 'Quil', 'hombre', 'Operacion', '567304')
returning rut, edad, nombre, apellido, genero , tratamiento, Rut_Doc;
"""
cur.execute(sql)
conn.commit()
pacientes = cur.fetchone()
print ("Insertamos los datos en pacientes :" )
print(pacientes)

sql=""" insert into pacientes(rut, edad, nombre, apellido, genero , tratamiento, Rut_Doc)
values ('986784', '12','Ignacio', 'Figueroa', 'hombre', 'Operacion', '98760')
returning rut, edad, nombre, apellido, genero , tratamiento, Rut_Doc;
"""
cur.execute(sql)
conn.commit()
pacientes = cur.fetchone()
print ("Insertamos los datos en pacientes :" )
print(pacientes)

sql=""" insert into pacientes(rut, edad, nombre, apellido, genero , tratamiento, Rut_Doc)
values ('4563', '27','Fernado', 'Perez','hombre', 'Vendaje', '98760')
returning rut, edad, nombre, apellido, genero , tratamiento, Rut_Doc;
"""
cur.execute(sql)
conn.commit()
pacientes = cur.fetchone()
print ("Insertamos los datos en pacientes :" )
print(pacientes)

sql=""" insert into pacientes(rut, edad, nombre, apellido, genero , tratamiento, Rut_Doc)
values ('12345','27', 'Jorge', 'Tapia', 'hombre', 'Vendaje', '98760')
returning rut, edad, nombre, apellido, genero , tratamiento, Rut_Doc;
"""
cur.execute(sql)
conn.commit()
pacientes = cur.fetchone()
print ("Insertamos los datos en pacientes :" )
print(pacientes)

sql=""" insert into enfermeros(rut, nombre, apellido, edad, genero, espec, Rut_CirDoc)
values ('456389', 'Gabriela', 'Hernandez', '29', 'mujer', 'cirugia ocular', '12345')
returning rut, nombre, apellido, edad, genero, espec, Rut_CirDoc;
"""
cur.execute(sql)
conn.commit()
enfermeros = cur.fetchone()
print ("Insertamos los datos en enfermeros :" )
print(enfermeros)

sql=""" insert into enfermeros(rut, nombre, apellido, edad, genero, espec, Rut_CirDoc)
values ('905783', 'Camila', 'Munoz','27','mujer' ,'cirugia  sinusoidal', '567304')
returning rut, nombre, apellido, edad, genero, espec, Rut_CirDoc;
"""
cur.execute(sql)
conn.commit()
enfermeros = cur.fetchone()
print ("Insertamos los datos en enfermeros :" )
print(enfermeros)
