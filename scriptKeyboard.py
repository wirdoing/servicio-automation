# -*- coding: utf-8 -*-
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

def presionarEnter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def abrirNuevaPestanaTerminal():
    keyboard.press(Key.ctrl)
    keyboard.press('t')
    keyboard.release(Key.ctrl)
    keyboard.release('t')
def transformarCarrera(carrera):
    if  carrera == 'LIC. EN CONTADURIA PUBLICA':
        return 1
    elif carrera == 'LIC. EN ECONOMIA':
        return 2
    elif carrera == 'LIC. EN GESTION Y ECONOMIA AMBIENTAL':
        return 3
    elif carrera == 'LIC. EN MERCADOTECNIA':
        return 4
    elif carrera == 'LIC. EN NEGOCIOS INTERNACIONALES':
        return 5
    elif carrera == 'LIC. EN RECURSOS HUMANOS':
        return 6
    elif carrera == 'LIC. EN TECNOLOGIAS DE INFORMACION':
        return 7
    elif carrera =='TURI':
        return 8
    elif carrera == ' LIC. EN TURISMO':
        return 8
    elif carrera == 'LIC. EN ADMINISTRACION':
        return 9
    elif carrera == 'LIC. EN GESTION DE NEGOCIOS GASTRONOMICOS':
        return 10
    elif carrera == 'LIC. EN RELACIONES PUBLICAS Y COMUNICACION':
        return 11
    elif carrera =='LIC. EN ADMINISTRACION FINANCIERA Y SISTEMAS':
        return 12
    elif carrera =='LAGP':
        return 13
    elif carrera ==' LIC. EN ADMINISTRACION GUBERNAMENTAL Y POLITICAS PUBLICAS':
        return 13
    elif carrera =='ING. EN NEGOCIOS':
        return 14
    elif carrera =='INTERCAMBIO':
        return 15
    elif carrera =='MAESTRIA EN ADMINISTRACION DE NEGOCIOS':
        return 16
    elif carrera =='MAESTRIA EN ECONOMIA':
        return 17
    elif carrera =='MAESTRIA EN FINANZAS EMPRESARIALES':
        return 18 
    elif carrera =='MAESTRIA EN NEGOCIOS INTERNACIONALES':
        return 19
    elif carrera =='MAESTRIA EN RELACIONES ECONOMICAS INTERNACIONALES Y COOPERACION CON ENFASIS EN AL-UE':
        return 20
    elif carrera =='MAESTRIA EN ANALISIS TRIBUTARIO':
        return 21
    elif carrera =='MAESTRIA EN EDUCACION SUPERIOR INTERNACIONAL':
        return 22
    elif carrera =='MAESTRIA EN GESTION DE LA SEGURIDAD Y SALUD EN EL TRABAJO':
        return 23
    elif carrera =='MAESTRIA EN POLITICAS PUBLICAS':
        return 24
    elif carrera == 'MAESTRIA EN TECNOLOGIAS DE LA INFORMACION':
        return 25
    elif carrera == 'MAESTRIA EN DIRECCION DE MERCADOTECNIA':
        return 26
    elif carrera =='MAESTRIA EN ESTUDIOS DEL TURISMO':
        return 27
    elif carrera =='MAESTRIA EN GESTION Y POLITICAS DE LA EDUCACION SUPERIOR':
        return 28
    elif carrera =='MAESTRIA EN NEGOCIOS Y ESTUDIOS ECONOMICOS':
        return 29
    elif carrera =='MAESTRIA EN TECNOLOGIAS PARA EL APRENDIZAJE':
        return 30
    elif carrera =='DOCTORADO EN CIENCIAS DE LA ADMINISTRACION':
        return 31
    elif carrera =='MAESTRÍA EN INNOVACIÓN SOCIAL Y GESTIÓN DEL BIENESTAR':#ojo esta no esta en el script
        return 38
    elif carrera =='DOCTORADO EN GESTION DE LA EDUCACION SUPERIOR':
        return 32
    elif carrera =='DOCTORADO EN ESTUDIOS ECONOMICOS':
        return 33
    elif carrera =='DOCTORADO EN POLITICAS PUBLICAS Y DESARROLLO':
        return 34
    elif carrera =='DOCTORADO EN ESTUDIOS FISCALES':
        return 35
    elif carrera =='DOCTORADO EN TECNOLOGIAS DE INFORMACION':
        return 36
    elif carrera == 'MAESTRIA EN RESOLUCIÓN DE CONFLICTOS':
        return 37
    elif carrera =='OTRO CENTRO DE UDG':
        return 38
    else:
        print("algo fallo")


def nuevaCuenta(login,nombre,apellido,carrera,ciclo,correo,curp,codigo):
    transformarCarrera(carrera)
    abrirNuevaPestanaTerminal()
    time.sleep(3)
    keyboard.type('ssh prestador@zimbra')
    presionarEnter()
    time.sleep(5)
    #keyboard.type('Team_Equipo_CUC34')
    #presionarEnter()
    #quitar comentarios a las 2 lineas pasadas si se elimina la contraseña en el ssh
    keyboard.type('2')
    presionarEnter()
    keyboard.type('2')
    presionarEnter()
    keyboard.type(login)
    presionarEnter()
    keyboard.type(nombre)
    presionarEnter()
    keyboard.type(apellido)
    presionarEnter()
    keyboard.type(transformarCarrera)
    presionarEnter()
    keyboard.type(ciclo)
    presionarEnter()
    keyboard.type(correo)
    presionarEnter()
    keyboard.type(curp)
    presionarEnter()
    keyboard.type(codigo)
    presionarEnter()
    time.sleep(5)