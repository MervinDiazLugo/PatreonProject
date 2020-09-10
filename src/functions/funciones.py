# -*- coding: utf-8 -*-
import re
from src.functions.config import Config

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OpcionesChrome

scenario = Config.Scenario

class Func():
    def abrir_navegador(self, link=Config.URL, navegador=Config.NAVEGADOR):
        if navegador == ("CHROME"):
            options = OpcionesChrome()
            options.add_argument('start-maximized')
            self.driver = webdriver.Chrome(chrome_options=options, executable_path=Config.basedir + "\\drivers\\chromedriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.get(link)
            return self.driver

    def replaceWithScenaryValues(self, text):
        patronDeBusqueda= r"(?<=Scenario:)\w+"
        variables= re.findall(str(patronDeBusqueda), text, re.IGNORECASE)
        for variable in variables:
            #text = re.sub('Scenario:', scenario[variable], text, re.IGNORECASE)
            text = re.sub('(Scenario:)' + variable,  scenario[variable], text, re.IGNORECASE)
            print("variable Scenario: " + text)
        return text

