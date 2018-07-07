from config import *
import psycopg2
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))

cur = conn.cursor()

sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql =  """CREATE TABLE salas(Nro_sala integer PRIMARY KEY , Tipo varchar, Piso varchar);"""

cur.execute(sql)

sql =  """CREATE TABLE doctores(
rut serial PRIMARY KEY , nombre varchar , apellido varchar, edad integer , genero varchar, Tipo_Cons varchar,
cirujano bit, Nro_salaDoc integer references salas(Nro_sala), fecha varchar);"""

cur.execute(sql)

sql = """ CREATE TABLE pacientes(rut serial PRIMARY KEY ,
edad integer, nombre varchar, apellido varchar, genero varchar,
tratamiento varchar , Rut_Doc serial references doctores(rut));"""

cur.execute(sql)

sql =  """CREATE TABLE enfermeros(rut serial PRIMARY KEY , nombre varchar , apellido varchar, edad integer,
genero varchar, espec varchar, Rut_CirDoc serial references doctores(rut));"""

cur.execute(sql)

conn.commit()
cur.close()
conn.close()
