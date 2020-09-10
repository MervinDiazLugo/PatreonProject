# -*- coding: utf-8 -*-
import unittest
import time
from src.functions.funciones import Func
from src.functions.config import Config
from selenium.webdriver.common.by import By

scenario = Config.Scenario

class tst_001(unittest.TestCase, Func):

    def setUp(self):
        self.driver = self.abrir_navegador()
        scenario["tag"] = self.driver.find_element(By.ID, "SIvCob").text

    def test_something(self):
        myTexy1 = Func.replaceWithScenaryValues(self,"Scenario:Periodo")
        myTexy2 = Func.replaceWithScenaryValues(self, "Scenario:tag")

        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(myTexy1)

        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@name='q']").clear()


        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(myTexy2)
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
