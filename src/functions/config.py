# -*- coding: utf-8 -*-
import os


class Config:
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    environment = 'test'


    if environment == 'test':

        NAVEGADOR = 'CHROME'
        URL = "https://www.google.com/"

        Scenario = {
            "TENANT_ID": "7852222",
            "TBASE": "MI BASE EN TEST",
            "Periodo": "Enero 2020",
            "Proceso": "Review 1500 (00002555)",
            "Proceso": "Review 170",
            "Empresa": "Empresa_0",
            "Modelo": "Todos"
        }

    if environment == 'dev':
        Scenario = {
            "TENANT_ID": "485666",
            "TBASE": "MI BASE EN DEV",
            "Periodo": "Enero 2019",
            "Proceso": "Review 250 (558996563)",
            "Proceso": "Review 170",
            "Empresa": "Empresa_0",
            "Modelo": "Todos"
        }


