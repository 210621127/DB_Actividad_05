PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE USUARIO(    correo TEXT NOT NULL,	contra TEXT NOT NULL,	apellidoPatU TEXT NOT NULL,	apellidoMatU TEXT,    nombresU TEXT NOT NULL,	PRIMARY KEY(correo));
INSERT INTO "USUARIO" VALUES('qwerty@gmail.com','qwe','Rodriguez','Bocanegra','Juan Daniel');
CREATE TABLE CONTACTO(	contacto_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,	email TEXT NOT NULL,	registra TEXT NOT NULL,	apellidoPatC TEXT NOT NULL,	apellidoMatC TEXT,	nombresC TEXT NOT NULL,	FOREIGN KEY(registra) REFERENCES USUARIO ( correo )    );
INSERT INTO "CONTACTO" VALUES(1,'juan_perez@gmail.com','qwerty@gmail.com','Perez','Lopez','Juan ');
INSERT INTO "CONTACTO" VALUES(2,'luis@gmail.com','qwerty@gmail.com','Chavez','','Luis');
CREATE TABLE CORREO(	correo_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,	fecha NUMERIC NOT NULL,	hora NUMERIC NOT NULL,	de TEXT NOT NULL,	para TEXT NOT NULL,    para_id INTEGER NOT NULL, 	texto TEXT,	asunto TEXT,	adjunto TEXT,    eliminado BOOLEAN NOT NULL,	FOREIGN KEY(`de`) REFERENCES USUARIO ( correo ),	FOREIGN KEY(`para_id`) REFERENCES CONTACTO ( contacto_id ));
INSERT INTO "CORREO" VALUES(1,'11/06/16','17:05:05','qwerty@gmail.com','juan_perez@gmail.com',1,'Hola Juan!
Solo te escribo par saludar...!
:v',NULL,NULL,0);
INSERT INTO "CORREO" VALUES(2,'11/06/16','17:11:53','qwerty@gmail.com','luis@gmail.com',2,'Hola
Saludos
:v',NULL,NULL,0);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('CONTACTO',2);
INSERT INTO "sqlite_sequence" VALUES('CORREO',2);
COMMIT;
