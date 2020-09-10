import time
from behave import *
from src.functions.funciones import Func
from src.functions.funciones import Config
from selenium.webdriver.common.by import By
use_step_matcher("re")

scenario = Config.Scenario

@given("Open Browser")
def step_impl(self):
    self.driver = Func.abrir_navegador(self)

@then("I save label (.*) as scenario context")
def step_impl(self, label):
    scenario[label] = self.driver.find_element(By.ID, label).text


@then("I set xpath (.*) with (.*)")
def step_impl(self, xpath, value):
    myTexy = Func.replaceWithScenaryValues(self, value)
    self.driver.find_element(By.XPATH, xpath).send_keys(myTexy)


@step("sleep (.*) seconds")
def step_impl(self, sec):
    time.sleep(int(sec))

