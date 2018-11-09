from cocomo import Cocomo

class CocomoModel():
    def __init__(self):
        self.tipo = Cocomo.Tipos.ORGANICO
        self.modelo = Cocomo.Modelo.BASICO
        self.esfuerzo = 0
        self.tiempo_desarrollo = 0
        self.personal = 0
        self.pr = 0
        self.kloc = 0

    def calcularEsfuerzo(self):
        pass

    def calcularTiempoDesarrollo(self):
        pass

    def calcularPersonal(self):
        pass

    def calcularPR(self):
        pass

    def calcularkloc(self):
        pass
