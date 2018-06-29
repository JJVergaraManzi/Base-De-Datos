from config import *
import psycopg2
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))

cur = conn.cursor()

sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql = """
CREATE TABLE paciente(rut serial PRIMARY KEY , edad integer, nombre varchar, apellido varchar, tratamiento varchar , Tipo_Cons varchar, Rut_Doc serial references doctor(rut), Rut_Cir serial references cirujano(rut));
CREATE TABLE sala(Nro_sala integer PRIMARY KEY , Tipo varchar, ID_Doc serial);
CREATE TABLE doctor(rut serial PRIMARY KEY , nombre varchar , apellido varchar, edad integer , Tipo_Cons varchar, Nro_salaDoc integer not null references sala(Nro_sala), dia varchar, horInit varchar, horFin varchar);
CREATE TABLE enfermero(rut serial PRIMARY KEY , nombre varchar , apellido varchar, edad integer , espec varchar, Rut_CirEnf serial not null references cirujano(rut));
CREATE TABLE cirujano(rut serial PRIMARY KEY , nombre varchar , apellido varchar, edad integer , espec varchar, Nro_salaCir integer not null references sala(Nro_sala), dia varchar, horInit varchar, horFin varchar);
CREATE TABLE atiende(NroSala_ID serial PRIMARY KEY, RutDoc_ID serial PRIMARY KEY);
"""

cur.execute(sql)
conn.commit()
cur.close()
conn.close()
