from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

variableOpcionDeMenu = '2'
variableDeAlta = '2'
loginTest = 'loginTest2'
nombreTest = 'nombreTest2'
apellidoTest = 'apellidoTest2'
carreraTest = '7'
cicloTest = '2019a'
correoAlternativoTest = 'hola254543587@gmail.com'
curpTest = 'dvbgfhleahkfue22a'
codigoTest = '21048497'


# time.sleep(5)
keyboard.type('ssh prestador@zimbra')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type(variableOpcionDeMenu)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type(variableDeAlta)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type(loginTest)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type(nombreTest)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type(apellidoTest)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type(carreraTest)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type(cicloTest)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type(correoAlternativoTest)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type(curpTest)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type(codigoTest)
keyboard.press(Key.enter)
keyboard.release(Key.enter)