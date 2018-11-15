import sys
from PyQt5.QtWidgets import QApplication, QStyleFactory
from enum import Enum
from cocomo import Cocomo
from cocomo_model import CocomoModel
from cocomo_view import CocomoView
import json


class CocomoController():
    def __init__(self):
        app = QApplication(sys.argv)
        self.view = CocomoView(self)
        self.modelo = CocomoModel(self, lambda esfuerzo, tiempo_desarrollo, personal, pr,
                                  loc, pf, di: self.view.mostrar_calculos_cocomo(esfuerzo, tiempo_desarrollo, personal, pr, loc, pf, di))
        #self.establecer_modelo_vista(self.modelo.modelo)
        #self.establecer_tipo_vista(self.modelo.tipo)
        #app.setStyle(QStyleFactory.create("Fusion"))
        print(type(self.modelo))
        sys.exit(app.exec_())

    def reestablecer_modelo(self):
        self.modelo.reset()

    def definir_modelo(self, modelo):
        print('Establecer' + str(modelo))
        self.modelo.establecer_modelo(modelo)

    def establecer_modelo_vista(self, modelo):
        self.view.cambiar_modelo(modelo)

    def definir_tipo(self, tipo):
        self.modelo.establecer_tipo(tipo)

    def establecer_tipo_vista(self, tipo):
        self.view.cambiar_tipo(tipo)

    def gti_cambiado(self, valores):
        try:
            self.modelo.calcularGti(valores)
        except AttributeError:
            pass

    def fae_cambiado(self, valores):
        try:
            self.modelo.calcularFae(valores)
        except AttributeError:
            pass
        # pass

    def cocomo_calculado(self, esfuerzo, tiempo_desarrollo, personal, pr, loc, pf, di):
        self.view.mostrar_calculos_cocomo(
            esfuerzo, tiempo_desarrollo, personal, pr, loc, pf, di)

    def calcularPf(self, entradas, salidas, peticiones, archivos, interfaces):
        self.modelo.calcularPf(
            entradas, salidas, peticiones, archivos, interfaces)

    def salvar(self, fileName):
        # with open(fileName, "w") as write_file:
        #    json.dump(model, write_file)
        pass

    def abrir(self, fileName):
        pass

    def definir_lenguaje_programacion(self, lenguajes):
        print(lenguajes)
        self.modelo.establecer_lenguajes(lenguajes)

if __name__ == '__main__':
    ccm = CocomoController()
