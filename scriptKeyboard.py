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

def nuevaCuenta(login,nombre,apellido,carreraTransformada,ciclo,correo,curp,codigo):
    #transformarCarrera(carrera)
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
    keyboard.type(carreraTransformada)
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