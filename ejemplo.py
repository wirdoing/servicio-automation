# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest,re, os
import scriptKeyboard
class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
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
                login = datos[17]
                nombre = datos[1]
                apellido = datos[3]
                carrera = datos[17]
                ciclo = datos[21]
                correo = datos[11]
                curp = datos[15]
                codigo = datos[9]
                scriptKeyboard.nuevaCuenta(login,nombre,apellido,carrera,ciclo,correo,curp,codigo)                    

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
        driver = self.driver
        driver.quit()
        

if __name__ == "__main__":
    unittest.main()