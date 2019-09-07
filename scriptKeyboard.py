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
        carrera=1
    elif carrera == 'LIC. EN ECONOMIA':
        carrera=2
    elif carrera == 'LIC. EN GESTION Y ECONOMIA AMBIENTAL':
        carrera=3
    elif carrera == 'LIC. EN MERCADOTECNIA':
        carrera=4
    elif carrera == 'LIC. EN NEGOCIOS INTERNACIONALES':
        carrera=5
    elif carrera == 'LIC. EN RECURSOS HUMANOS':
        carrera=6
    elif carrera == 'LIC. EN TECNOLOGIAS DE INFORMACION':
        carrera=7
    elif carrera =='TURI':
        carrera=8
    elif carrera == ' LIC. EN TURISMO':
        carrera=8
    elif carrera == 'LIC. EN ADMINISTRACION':
        carrera=9
    elif carrera == 'LIC. EN GESTION DE NEGOCIOS GASTRONOMICOS':
        carrera=10
    elif carrera == 'LIC. EN RELACIONES PUBLICAS Y COMUNICACION':
        carrera=11
    elif carrera =='LIC. EN ADMINISTRACION FINANCIERA Y SISTEMAS':
        carrera=12
    elif carrera =='LAGP':
        carrera=13
    elif carrera ==' LIC. EN ADMINISTRACION GUBERNAMENTAL Y POLITICAS PUBLICAS':
        carrera=13
    elif carrera =='ING. EN NEGOCIOS':
        carrera=14
    elif carrera =='INTERCAMBIO':
        carrera=15
    elif carrera =='MAESTRIA EN ADMINISTRACION DE NEGOCIOS':
        carrera=16
    elif carrera =='MAESTRIA EN ECONOMIA':
        carrera=17
    elif carrera =='MAESTRIA EN FINANZAS EMPRESARIALES':
        carrera=18 
    elif carrera =='MAESTRIA EN NEGOCIOS INTERNACIONALES':
        carrera=19
    elif carrera =='MAESTRIA EN RELACIONES ECONOMICAS INTERNACIONALES Y COOPERACION CON ENFASIS EN AL-UE':
        carrera=20
    elif carrera =='MAESTRIA EN ANALISIS TRIBUTARIO':
        carrera=21
    elif carrera =='MAESTRIA EN EDUCACION SUPERIOR INTERNACIONAL':
        carrera=22
    elif carrera =='MAESTRIA EN GESTION DE LA SEGURIDAD Y SALUD EN EL TRABAJO':
        carrera=23
    elif carrera =='MAESTRIA EN POLITICAS PUBLICAS':
        carrera=24
    elif carrera == 'MAESTRIA EN TECNOLOGIAS DE LA INFORMACION':
        carrera=25
    elif carrera == 'MAESTRIA EN DIRECCION DE MERCADOTECNIA':
        carrera=26
    elif carrera =='MAESTRIA EN ESTUDIOS DEL TURISMO':
        carrera=27
    elif carrera=='MAESTRIA EN GESTION Y POLITICAS DE LA EDUCACION SUPERIOR':
        carrera=28
    elif carrera =='MAESTRIA EN NEGOCIOS Y ESTUDIOS ECONOMICOS':
        carrera=29
    elif carrera =='MAESTRIA EN TECNOLOGIAS PARA EL APRENDIZAJE':
        carrera=30
    elif carrera=='DOCTORADO EN CIENCIAS DE LA ADMINISTRACION':
        carrera=31
    elif carrera=='MAESTRÍA EN INNOVACIÓN SOCIAL Y GESTIÓN DEL BIENESTAR':#ojo esta no esta en el script
        carrera=38
    elif carrera=='DOCTORADO EN GESTION DE LA EDUCACION SUPERIOR':
        carrera=32
    elif carrera =='DOCTORADO EN ESTUDIOS ECONOMICOS':
        carrera=33
    elif carrera =='DOCTORADO EN POLITICAS PUBLICAS Y DESARROLLO':
        carrera=34
    elif carrera =='DOCTORADO EN ESTUDIOS FISCALES':
        carrera=35
    elif carrera =='DOCTORADO EN TECNOLOGIAS DE INFORMACION':
        carrera=36
    elif carrera == 'MAESTRIA EN RESOLUCIÓN DE CONFLICTOS':
        carrera=37
    elif carrera =='OTRO CENTRO DE UDG':
        carrera=38


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
    keyboard.type(carrera)
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