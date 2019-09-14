# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
import unittest,re,os
import scriptKeyboard
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
        self.driver = webdriver.Firefox(options=options)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://ayuda.cucea.udg.mx/")
        driver.find_element_by_id("usuario").clear()
        driver.find_element_by_id("usuario").send_keys("melissa.carrillo")
        driver.find_element_by_id(u"contraseña").click()
        driver.find_element_by_id(u"contraseña").clear()
        driver.find_element_by_id(u"contraseña").send_keys("Melivonne7430")
        driver.find_element_by_id("ingresar").click()
        lista = driver.find_elements_by_xpath("//td[text()='Cuenta de Correo Institucional']/following-sibling::td[text()='En espera']/preceding-sibling::td[1]")
        lista_de_listas=[lista[i:i+1] for i in range (0, len(lista))]
        #for element in lista_de_listas:
         #   print(element.text)
        for element in lista_de_listas:
            for element in element:
                var=element.text
                print(var)
                datos=var.split('\n')
                print(datos)
                login = datos[19]
                nombre = datos[1]
                apellido = datos[3]
                carrera = datos[17]
                ciclo = datos[21]
                correo = datos[11]
                curp = datos[15]
                codigo = datos[9]
                tipo_de_cuenta = datos[13]
                departamento = datos[6]
                if tipo_de_cuenta == 'Alumno' : 
                    carreraTransformada=transformarCarrera(carrera)
                    scriptKeyboard.nuevaCuentaAlumno(login,nombre,apellido,carreraTransformada,ciclo,correo,curp,codigo)
                elif tipo_de_cuenta == 'Profesor' or tipo_de_cuenta == 'Personal Administrativo' or tipo_de_cuenta == 'Personal Académico':
                    scriptKeyboard.nuevaCuentaAdmin(login,nombre,apellido,departamento,codigo,correo)
                
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
        driver = self.driver
        driver.quit()
        

if __name__ == "__main__":
    unittest.main()