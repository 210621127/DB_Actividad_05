"""
Nombre: Rodriguez Bocanegra, Juan Daniel
Materia: Seminario de Solucion de Problemas de Bases de datos
Profesor: Michel Davalos Boites

Actividad 05 (INSERT INTO)
Implementar todos los "INSERT" que requiere el software: correo nuevo,
crear contacto, etc. Subir reporte con capturas de pantalla de la ejecución
del programa, el .sql y el .py (o repositorio).
"""
import sqlite3
import os
import time
import getpass

class Usuario():
    def __init__(self, data):
        self.correo = data
        self.contra = data
        self.apellidoPatU = data
        self.apellidoMatU = data
        self.nombresU = data
        self.contRegistrados = 0
    def __str__ (self):
        return "\n\tCorreo: "+str(self.correo)+"\n\tContraseña: "+str(self.contra)\
            +"\n\tNombre: "+str(self.apellidoPatU)+" "+str(self.apellidoMatU)+","\
            +str(self.nombresU)+"\n\tContactos registrados: "+str(self.contRegistrados)

class Contacto():
    def __init__(self,data):
        self.email = data
        self.contacto_id = data
        self.registra = data
        self.apellidoPatC = data
        self.apellidoMatC = data
        self.nombresC = data

class Correo():
    def __init__(self, data):
        self.correo_id = data
        self.fecha = data
        self.hora = data
        self.de = data
        self.para = data
        self.texto = data
        self.adjunto = data

class MenuCorreoEnviado():
    def __init__(self):
        pass

class MenuContatos():
    c = Contacto(None)

    def __init__(self):
        pass
    def agregar(self):
        c = Contacto(None)
        os.system("clear")
        print("\n\t- - - Agregar contacto - - -\n")

        c.email = input("\n\tIngrese el correo del contacto: ")
        while len(c.email) < 5:
            print("\n\t(!) Ingrese un correo valido!")
            c.email = input ("\tCorreo: ")




        input("\n\tPresione una tecla para continuar...")


    def menu(self):
        opc = -1
        while True:
            os.system("clear")
            print("\t* * * CONTACTOS * * * \n")
            #print("\n\t1) Mostrar contactos ") # Muestra contactos - con id-
            print("\t2) Agregar nuevo contacto") #Agrega un nuevo contacto -correo-
            #print("\t3) Eliminar contacto") # Elimina de la base de datos (submenu)
            #print("\t4) Modificar contacto") # Modifica un contacto (submenu)
            print("\t0) Salir")
            opc = input ("\n\tIngrese una opcion: ")
            if opc.isdigit() == True:
                opc = int(opc)
                if opc == 1:
                    pass
                elif opc == 2:
                    self.agregar()
                elif opc == 3:
                    pass
                elif opc == 4:
                    pass
                elif opc == 0:
                    db.commit()
                    break


class MenuCorreoNuevo():
    def __init (self):
        pass


class MainMenu():


    def __init__(self):
        pass
    def menuGeneral(self,u,db):
        mNuevo = MenuCorreoNuevo()
        mEnviado = MenuCorreoEnviado()
        mContactos = MenuContatos()
        db = db
        op = -1
        while True:
            os.system("clear")
            print("\n\tMENU GENERAL CORREOS\n\n\t1) Correo enviado\n\t2) Contactos \
                \n\t3) Correo nuevo\n\t0) Salir")
            op = input("\n\tOpcion:")
            while op.isdigit() == False:
                op = input("\n\t(!) Ingrese una opcion del menu: ")

            op = int(op)

            if op == 1:
                os.system("clear")
                pass
            elif op == 2:
                os.system("clear")
                mContactos.menu()
            elif op == 3:
                os.system("clear")
                pass
            elif op == 0:
                db.commit()
                break
            else:
                input("\n\t(!) Ingrese una opcion del menu...")

class Login_Registro():
    db = sqlite3.connect("db_correos.db")
    #c = db.cursor(), c.execute("PRAGMA foreign_keys = ON")

    mg = MainMenu()
    user = Usuario(None)

    def __init__(self):
        pass

    def login(u,db):
        while True:
            u = u
            db = db
            c = db.cursor()

            os.system("clear")
            print("\n\t* * * LOGIN * * *\n\t(Presione <ENTER> para regresar)")
            usuario = input("\n\tUsuario: ")
            if usuario == '':
                break
            contra = getpass.getpass ("\n\tContraseña: ")

            rows = c.execute ('SELECT * FROM USUARIO WHERE correo = ? AND \
                contra = ?',(usuario, contra))
            input("p")
            print ("rows: ", c.fetchone())

            if c.fetchall():
                input("\n\tLogin correcto!")
                for row in rows:
                    u.correo = row[0]
                    u.contra = row[1]
                    u.apellidoPatU = row[2]
                    u.apellidoMatU = row[3]
                    u.nombresU = row[4]
                    u.contRegistrados = row[5]

                print(u)
                input("...")
                return True
            else:
                input("\n\t(!) Usuario o contraseña incorrectos!!")

    def registrarse(u,d):
        user = u
        db = d
        c = db.cursor()
        while True:
            print("\n\t* * * Registro * * * \n\t(Presione <ENTER> para regresar)")
            user.correo = input ("\n\tCorreo: ")
            if user.correo == '':
                break

            while True:
                pass1 = getpass.getpass("\tContrañena: ")
                pass2 = getpass.getpass("\tIngrese de nuevo la contraseña: ")
                if pass1 != pass2 :
                    print("\n\t(!) Las contraseñas no coinciden!")
                if len(pass1) < 1:
                    print("\n\t(!) Ingrese una contraseña valida")
                else:
                    if pass1 == pass2:
                        user.contra = pass1
                        break

            user.apellidoPatU = input("\tApellido paterno: ")
            while user.apellidoPatU.isalnum() == False:
                print("\n\t(!) Apellido invalido!")
                user.apellidoPatU = input ("\tIngrese su apellido paterno de nuevo: ")

            user.apellidoMatU = input("\tApellido Materno: ")

            user.nombresU = input("\tNombre(s): ")
            while len(user.nombresU) < 1:
                print("(!) Nombre invalido!")
                user.nombresU = input("\tIngrese su nombre de nuevo: ")
            c.execute("INSERT INTO USUARIO (correo,contra,apellidoPatU,\
                apellidoMatU,nombresU,contRegistrados) VALUES (?,?,?,?,?,?)",\
                (user.correo, user.contra,user.apellidoPatU,user.apellidoMatU,\
                user.nombresU,user.contRegistrados))
            db.commit()
            break

    while True:
        os.system("clear")
        print("\n\t* * * INICIO DE SESION/REGISTRO * * * \n\n\t1) Iniciar sesion \
            \n\t2) Registrarse \n\t0) Salir")
        op = input("\n\tElige una opcion: ")

        while op.isdigit() == False:
            op = input ("(!) Ingrese una de las opciones: ")

        op = int (op)

        if op == 1:
            os.system("clear")
            if login(user,db) == True:
                mg.menuGeneral(user,db)

        elif op == 2:
            os.system("clear")
            registrarse(user,db)

        elif op == 0:
            db.close()
            exit()
