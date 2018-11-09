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
        self.fae = 1
        self.gti = 0
        self.pf = 0

    def calcularCocomo(self):
        pass

    def calcularFae(self, valores):
        self.fae = 1
        for val in valores:
            self.fae = self.fae * val

        return self.fae

    def calcularGti(self, valores):
        self.gti = 0
        for val in valores:
            self.gti = self.gti + val

        return self.gti
        

    def calcularPf(self, entradas, salidas, peticiones, archivos, interfaces):
        self.pf = 0

