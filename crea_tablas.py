import sqlite3
import os

os.remove("db_correos.db")

db = sqlite3.connect("db_correos.db")
c = db.cursor()

c.execute("CREATE TABLE USUARIO(\
    correo TEXT NOT NULL,\
	contra TEXT NOT NULL,\
	apellidoPatU TEXT NOT NULL,\
	apellidoMatU TEXT,\
    nombresU TEXT NOT NULL,\
	contRegistrados INTEGER NOT NULL,\
	PRIMARY KEY(correo)\
)")

c.execute("CREATE TABLE CONTACTO(\
	email TEXT NOT NULL,\
	contacto_id INTEGER NOT NULL,\
	registra TEXT NOT NULL,\
	apellidoPatC TEXT NOT NULL,\
	apellidoMatC TEXT,\
	nombresC TEXT NOT NULL,\
	PRIMARY KEY(email,registra),\
	FOREIGN KEY(contacto_id) REFERENCES USUARIO ( contRegistrados ),\
	FOREIGN KEY(registra) REFERENCES USUARIO ( correo )\
    )")

c.execute("CREATE TABLE CORREO(\
	correo_id INTEGER NOT NULL,\
	fecha NUMERIC NOT NULL,\
	hora NUMERIC NOT NULL,\
	de TEXT NOT NULL,\
	para TEXT NOT NULL,\
	texto TEXT,\
	asunto TEXT,\
	adjunto TEXT,\
    eliminado BOOLEAN NOT NULL,\
	PRIMARY KEY(correo_id),\
	FOREIGN KEY(`de`) REFERENCES USUARIO ( correo ),\
	FOREIGN KEY(`para`) REFERENCES CONTACTO ( email )\
)")

db.close()
