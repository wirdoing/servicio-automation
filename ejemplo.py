# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import unittest,re,os,time
import scriptKeyboard
import tkinter as tk
def escribirAuxiliar(c):
    escribir=open("auxiliar.txt","w")
    escribir.write(c)
    escribir.close
def identificarTipodeCuenta(tipo_de_cuenta):
    diccionario = {
        'Alumno' : '2',
        'Profesor' : '1',
        'Personal Administrativo' : '1',
        'Personal Académico' : '1'
    }
    cuentaIdentificada = diccionario[tipo_de_cuenta]
    return cuentaIdentificada
def transformarCarrera(carrera):
    diccionario = {
        'LIC. EN CONTADURIA PUBLICA':'1',    
        'LIC. EN ECONOMIA':'2',
        'LIC. EN GESTION Y ECONOMIA AMBIENTAL':'3',
        'LIC. EN MERCADOTECNIA':'4',
        'LIC. EN NEGOCIOS INTERNACIONALES':'5',
        'LIC. EN RECURSOS HUMANOS':'6',
        'LIC. EN TECNOLOGIAS DE INFORMACION':'7',
        'TURI':'8',
        ' LIC. EN TURISMO':'8',
        'LIC. EN ADMINISTRACION':'9',
        'LIC. EN GESTION DE NEGOCIOS GASTRONOMICOS':'10',
        'LIC. EN RELACIONES PUBLICAS Y COMUNICACION':'11',
        'LIC. EN ADMINISTRACION FINANCIERA Y SISTEMAS':'12',
        'LAGP':'13',
        ' LIC. EN ADMINISTRACION GUBERNAMENTAL Y POLITICAS PUBLICAS':'13',
        'ING. EN NEGOCIOS':'14',
        'INTERCAMBIO':'15',
        'MAESTRIA EN ADMINISTRACION DE NEGOCIOS':'16',
        'MAESTRIA EN ECONOMIA':'17',
        'MAESTRIA EN FINANZAS EMPRESARIALES':'18 ',
        'MAESTRIA EN NEGOCIOS INTERNACIONALES':'19',
        'MAESTRIA EN RELACIONES ECONOMICAS INTERNACIONALES Y COOPERACION CON ENFASIS EN AL-UE':'20',
        'MAESTRIA EN ANALISIS TRIBUTARIO':'21',
        'MAESTRIA EN EDUCACION SUPERIOR INTERNACIONAL':'22',
        'MAESTRIA EN GESTION DE LA SEGURIDAD Y SALUD EN EL TRABAJO':'23',
        'MAESTRIA EN POLITICAS PUBLICAS':'24',
        'MAESTRIA EN TECNOLOGIAS DE LA INFORMACION':'25',
        'MAESTRIA EN DIRECCION DE MERCADOTECNIA':'26',
        'MAESTRIA EN ESTUDIOS DEL TURISMO':'27',
        'MAESTRIA EN GESTION Y POLITICAS DE LA EDUCACION SUPERIOR':'28',
        'MAESTRIA EN NEGOCIOS Y ESTUDIOS ECONOMICOS':'29',
        'MAESTRIA EN TECNOLOGIAS PARA EL APRENDIZAJE':'30',
        'DOCTORADO EN CIENCIAS DE LA ADMINISTRACION':'31',
        'MAESTRÍA EN INNOVACIÓN SOCIAL Y GESTIÓN DEL BIENESTAR':'38',#ojo esta no esta en el script
        'DOCTORADO EN GESTION DE LA EDUCACION SUPERIOR':'32',
        'DOCTORADO EN ESTUDIOS ECONOMICOS':'33',
        'DOCTORADO EN POLITICAS PUBLICAS Y DESARROLLO':'34',
        'DOCTORADO EN ESTUDIOS FISCALES':'35',
        'DOCTORADO EN TECNOLOGIAS DE INFORMACION':'36',
        'MAESTRIA EN RESOLUCIÓN DE CONFLICTOS':'37',
        'OTRO CENTRO DE UDG':'38'
    }
    carreraTransformada=diccionario[carrera]
    return carreraTransformada
class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        #self.driver = webdriver.Firefox(options=options)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        root = tk.Tk()
        root.withdraw()
        driver = self.driver
        driver.maximize_window()
        driver.get("https://ayuda.cucea.udg.mx/")
        driver.find_element_by_id("usuario").clear()
        driver.find_element_by_id("usuario").send_keys("melissa.carrillo")
        driver.find_element_by_id(u"contraseña").click()
        driver.find_element_by_id(u"contraseña").clear()
        driver.find_element_by_id(u"contraseña").send_keys("Melivonne7430")
        driver.find_element_by_id("ingresar").click()
        botones = driver.find_elements_by_xpath("//td[text()='Cuenta de Correo Institucional']/following-sibling::td[text()='En espera']/following-sibling::td[7]/button[1]")
        lista = driver.find_elements_by_xpath("//td[text()='Cuenta de Correo Institucional']/following-sibling::td[text()='En espera']/preceding-sibling::td[1]")
        lista_de_listas=[lista[i:i+1] for i in range (0, len(lista))]
        numero_de_tickets=0
        #meter en un if para que no lo haga si no encuentra tickets
        driver.execute_script("window.open('https://zimbra.cucea.udg.mx');")
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("oscar.campos")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("Correozimbra123")
        driver.find_element_by_xpath("//input[@class='ZLoginButton DwtButton']").click()
        time.sleep(1)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        for element in lista_de_listas:
            for element in element:
                ##print(len(lista_de_listas))
                var=element.text
                ##print(var)
                datos=var.split('\n')
                ##print(datos)
                try:
                    login = datos[19]
                    nombre = datos[1]
                    apellido = datos[3]
                    carrera = datos[17]
                    ciclo = datos[21]
                    correo = datos[11]
                    curp = datos[15]
                    codigo = datos[9]
                    tipo_de_cuenta = datos[13]
                    departamento = datos[7]
                except:
                    #print("El ticket no fue capturado correctamente revisar por favor")
                    dateTimeObj = datetime.now()
                    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
                    f= open("operaciones.log","a+")
                    f.write(timestampStr+" El ticket fue capturado incorrectamente: "+login+" \n")
                    f.close
                if tipo_de_cuenta == 'Alumno' : 
                    carreraTransformada=transformarCarrera(carrera)
                    scriptKeyboard.nuevaCuentaAlumno(login,nombre,apellido,carreraTransformada,ciclo,correo,curp,codigo)
                    c = root.clipboard_get()#obtener lo copiado del clipboard
                    escribirAuxiliar(c)
                    count = len(open("auxiliar.txt").readlines(  ))
                    with open("auxiliar.txt", "r") as a:
                        lines = a.readlines()
                        try:
                            contra=lines[count-6]#la linea donde esta el usuario y contraseña
                            separador=contra.split(' ')#separar la lista por espacios
                            #print (lines[count-6])#linea para verificar si esta correcta la posicion del password
                            passoword=separador[8]
                            #print("Este es el password: "+passoword)
                            dateTimeObj = datetime.now()
                            timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
                            f= open("operaciones.log","a+")
                            f.write(timestampStr+" Creacion de cuenta de alumno: "+login+" \n")
                            f.close
                            botones[numero_de_tickets].click()
                            driver.find_element_by_xpath("//option[contains(text(),'Finalizado')]").click()
                            driver.find_element_by_id("coment").click()
                            driver.find_element_by_id("coment").clear()
                            driver.find_element_by_id("coment").send_keys("Usuario creado y email enviado")
                            driver.find_element_by_id("actualizar").click()
                            driver.find_element_by_id("bt-cierre").click()
                            driver.get("https://zimbra.cucea.udg.mx")
                            time.sleep(1)
                            driver.find_element_by_id("zb__NEW_MENU_title").click()
                            driver.find_element_by_id("zv__COMPOSE-1_to_control").clear()
                            driver.find_element_by_id("zv__COMPOSE-1_to_control").send_keys(correo)
                            driver.find_element_by_id("zv__COMPOSE-1_subject_control").click()
                            driver.find_element_by_id("zv__COMPOSE-1_subject_control").clear()
                            driver.find_element_by_id("zv__COMPOSE-1_subject_control").send_keys("Creacion de  correo institucional")
                            driver.find_element_by_xpath("//iframe[@id='ZmHtmlEditor1_body_ifr']").click()
                            #driver.find_element_by_xpath("//iframe[@id='ZmHtmlEditor1_body_ifr']").clear()
                            driver.find_element_by_xpath("//iframe[@id='ZmHtmlEditor1_body_ifr']").send_keys("Usuario: "+login+"\nPassword: "+passoword)
                            #driver.find_element_by_xpath("//div[@id='mceu_39']").send_keys("Login: "+login+"\nContraseña: "passoword)
                            driver.find_element_by_id("zb__COMPOSE-1__SEND_title").click()# enviar
                        except:
                            print("esta cuenta ya existe except")
                            dateTimeObj = datetime.now()
                            timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
                            f= open("operaciones.log","a+")
                            f.write(timestampStr+" Esta cuenta ya existe: "+login+" \n")
                            f.close
                            pass
                    a.close
                    os.remove("auxiliar.txt")
                    numero_de_tickets=numero_de_tickets+1
                elif tipo_de_cuenta == 'Profesor' or tipo_de_cuenta == 'Personal Administrativo' or tipo_de_cuenta == 'Personal Académico':
                    #todo: especificar el login de este case
                    separaNombre=nombre.split(' ')
                    primerNombre=separaNombre[0]
                    separaApellido=apellido.split(' ')
                    primerApellido=separaApellido[0]
                    loginAdmin=primerNombre+"."+primerApellido
                    scriptKeyboard.nuevaCuentaAdmin(loginAdmin,nombre,apellido,departamento,codigo,correo)
                    c = root.clipboard_get()#obtener lo copiado del clipboard
                    escribirAuxiliar(c)
                    count = len(open("auxiliar.txt").readlines(  ))
                    with open("auxiliar.txt", "r") as a:
                        lines = a.readlines()
                        try:
                            contra=lines[count-2]#la linea donde esta el usuario y contraseña
                            separador=contra.split(' ')#separar la lista por espacios
                            #print (lines[count-2])#linea para verificar si esta correcta la posicion del password
                            passoword=separador[8]
                            #print("Este es el password: "+passoword)
                            dateTimeObj = datetime.now()
                            timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
                            f= open("operaciones.log","a+")
                            f.write(timestampStr+" Creacion de cuenta de "+tipo_de_cuenta+" :"+login+" \n")
                            f.close
                            botones[numero_de_tickets].click()
                            driver.find_element_by_xpath("//option[contains(text(),'Finalizado')]").click()
                            driver.find_element_by_id("coment").click()
                            driver.find_element_by_id("coment").clear()
                            driver.find_element_by_id("coment").send_keys("Usuario creado y email enviado")
                            driver.find_element_by_id("actualizar").click()
                            driver.find_element_by_id("bt-cierre").click()
                            driver.get("https://zimbra.cucea.udg.mx")
                            time.sleep(1)
                            driver.find_element_by_id("zb__NEW_MENU_title").click()
                            driver.find_element_by_id("zv__COMPOSE-1_to_control").clear()
                            driver.find_element_by_id("zv__COMPOSE-1_to_control").send_keys(correo)
                            driver.find_element_by_id("zv__COMPOSE-1_subject_control").click()
                            driver.find_element_by_id("zv__COMPOSE-1_subject_control").clear()
                            driver.find_element_by_id("zv__COMPOSE-1_subject_control").send_keys("Creacion de  correo institucional")
                            driver.find_element_by_xpath("//iframe[@id='ZmHtmlEditor1_body_ifr']").click()
                            #driver.find_element_by_xpath("//iframe[@id='ZmHtmlEditor1_body_ifr']").clear()
                            driver.find_element_by_xpath("//iframe[@id='ZmHtmlEditor1_body_ifr']").send_keys("Usuario: "+login+
                            "\nPassword: "+passoword+"\nCorreo electronico: "+login+"@alumnos.cucea.udg.mx")
                            #driver.find_element_by_xpath("//div[@id='mceu_39']").send_keys("Login: "+login+"\nContraseña: "passoword)
                            driver.find_element_by_id("zb__COMPOSE-1__SEND_title").click()# enviar                            
                        except:
                            print("esta cuenta ya existe except")
                            dateTimeObj = datetime.now()
                            timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
                            f= open("operaciones.log","a+")
                            f.write(timestampStr+" Esta cuenta ya existe: "+login+" \n")
                            f.close                            
                            pass
                    dateTimeObj = datetime.now()
                    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")
                    f= open("operaciones.log","a+")
                    f.write(timestampStr+" Creacion de cuenta de "+tipo_de_cuenta+" y su login es: "+login+" \n")
                    f.close
                    #print("Solo elemento: "+element)
                    #print("lista de listas: "+lista_de_listas)
                    botones[numero_de_tickets].click()
                    numero_de_tickets=numero_de_tickets+1
    """ def test2(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com.mx") """
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
        driver = self.driver
        driver.quit()
        

if __name__ == "__main__":
    unittest.main()