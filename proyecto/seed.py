from config import *
from datetime import datetime
import psycopg2

conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()

sql = """
insert into paciente (nombre ,rut , edad , apellido , tratamiento , Tipo_Cons , Rut_Doc, Rut_Cir )
values ('Juan ', '0', '23' , 'Perez', 'Gotas Oculares','Oftalmologia', '1', NULL)
returning
nombre ,rut , edad , apellido , tratamiento , Tipo_Cons , Rut_Doc, Rut_Cir;
"""

cur.execute(sql)
conn.commit()
pac = cur.fetchone()
print ("Insertamos los datos en paciente :" )
print(pac)

sql = """
insert into doctor (nombre ,rut , edad , apellido , Tipo_Cons ,Nro_salaDoc,dia , horInit , horFin)
values ('Gonzalo', '1', '35' , 'Gonzalez', 'tp_test1', '312', )
returning
nombre ,rut , edad , apellido , Tipo_Cons ,Nro_salaDoc,dia ,horInit , horFin;
"""

cur.execute(sql)
conn.commit()
doc = cur.fetchone()
print ("Insertamos los datos en doctor :" )
print(doc)

sql = """
insert into sala (Nro_sala , Tipo)
values ('312', 'consulta' )
returning
Nro_sala , Tipo ,  dia , horInit , horFin;
"""

cur.execute(sql)
conn.commit()
sala = cur.fetchone()
print ("Insertamos los datos en sala :" )
print(sala)

sql = """
insert into cirujano(rut, nombre, apellido, edad, espec, Nro_salaCir,dia , horInit , horFin )
values ('2', 'Cir_Test', 'CirAp_Test', '40', 'traumatologo', '5' )
returning
rut, nombre, apellido, edad, espec, Nro_salaCir,dia , horInit , horFin;
"""

cur.execute(sql)
conn.commit()
ciruj = cur.fetchone()
print ("Insertamos los datos en cirujano :" )
print(ciruj)

sql = """
insert into sala (Nro_sala , Tipo )
values ('5', 'operacion')
returning
Nro_sala , Tipo ,  ;
"""

cur.execute(sql)
conn.commit()
sala = cur.fetchone()
print ("Insertamos los datos en sala :" )
print(sala)

sql = """
insert into enfermero(rut, nombre, apellido, edad, espec, Rut_CirEnf, dia , horInit , horFin)
values ('8', 'Enf_Test', 'EnfAp_Test', '34', 'traumatologo', '2' )
returning
rut, nombre, apellido, edad, espec, Nro_salaCir;
"""

cur.execute(sql)
conn.commit()
enferm = cur.fetchone()
print ("Insertamos los datos en cirujano :" )
print(enferm)
