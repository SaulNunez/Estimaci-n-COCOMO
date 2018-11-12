import sys
from PyQt5.QtWidgets import QApplication, QStyleFactory
from enum import Enum
from cocomo import Cocomo
from cocomo_model import CocomoModel
from cocomo_view import CocomoView

def iniciar():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    model = CocomoModel()
    view = CocomoView()
    sys.exit(app.exec_())

def reestablecer_modelo():
    pass

def fae_cambiado(valores):
    pass

def gti_cambiado(valores):
    pass

def calcularPf(entradas, salidas, peticiones, archivos, interfaces):
    pass

if __name__ == '__main__':
    iniciar()