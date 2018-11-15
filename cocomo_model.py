from cocomo import Cocomo


class CocomoModel():
    def __init__(self, controller, correr_al_calcular):
        self.reset()
        self.correr_al_calcular = correr_al_calcular

    def reset(self):
        self.__tipo = Cocomo.Tipo.ORGANICO
        self.tipo = property(self.tipo, self.establecer_tipo)
        self.modelo = property(self.modelo, self.establecer_modelo)
        self.lenguajes = property(self.lenguajes, self.establecer_lenguajes)
        self.__modelo = Cocomo.Modelo.BASICO
        self.__esfuerzo = 0
        self.__tiempo_de_desarrollo = 0
        self.__personal = 0
        self.__pr = 0
        self.loc = 0
        self.__fae = 1
        self.gti = 0
        self.pf = 0
        self.__lenguajes = []

    def tipo(self):
        return self.__tipo

    def establecer_tipo(self, tipo):
        self.__tipo = tipo
        self.calcularCocomo()

    def modelo(self):
        return self.__modelo

    def establecer_modelo(self, modelo):
        self.__modelo = modelo
        print('Establecido' + str(self.__modelo))
        self.calcularCocomo()

    def lenguajes(self):
        return self.__lenguajes

    def establecer_lenguajes(self, lenguajes):
        print("hol")
        print(lenguajes)
        self.__lenguajes = lenguajes
        self.calcular_loc()

    def calcular_loc(self):
        self.loc = 0
        for lenguaje in self.__lenguajes:
            self.loc += self.pf * Cocomo.indice_loc[lenguaje]
        print("Lineas" + str(self.loc))
    
    def calcularCocomo(self):
        a = Cocomo.constantes[self.__modelo][self.__tipo]['a']
        b = Cocomo.constantes[self.__modelo][self.__tipo]['b']
        c = Cocomo.constantes[self.__modelo][self.__tipo]['c']
        d = Cocomo.constantes[self.__modelo][self.__tipo]['d']
        self.__esfuerzo = a * (self.loc / 1000) ** b
        if(self.__modelo == Cocomo.Modelo.INTERMEDIO):
            self.__esfuerzo = self.__esfuerzo * self.__fae
        self.__tiempo_de_desarrollo = c * self.__esfuerzo ** d
        if self.__tiempo_de_desarrollo != 0:
            self.__personal = self.__esfuerzo/self.__tiempo_de_desarrollo
        else:
            self.__personal = 0
        if self.__esfuerzo != 0:
            self.__pr = self.loc / self.__esfuerzo
        else:
            self.__pr = 0

        self.calcular_loc()
        self.correr_al_calcular(self.__esfuerzo, self.__tiempo_de_desarrollo, self.__personal, self.__pr, self.loc)

    def calcularGti(self, valores):
        self.gti = 0
        for val in valores:
            self.gti = self.gti + val
        print("Grado total de influencia" + str(self.gti))
        self.calcularCocomo()

    def calcularPf(self, entradas, salidas, peticiones, archivos, interfaces):
        self.pf = 0
        if(entradas < 4):
            entradas_total = entradas * 3
        elif(entradas < 6):
            entradas_total = entradas * 4
        else:
            entradas_total = entradas * 6

        if(salidas < 5):
            salidas_total = salidas * 4
        elif(salidas < 7):
            salidas_total = salidas * 5
        else:
            salidas_total = salidas * 7

        if(peticiones < 4):
            peticiones_total = peticiones * 3
        elif(peticiones < 6):
            peticiones_total = peticiones * 4
        else:
            peticiones_total = peticiones * 6

        if(archivos < 10):
            archivos_total = archivos * 7
        elif(archivos < 15):
            archivos_total = archivos * 10
        else:
            archivos_total = archivos * 15

        if(interfaces < 7):
            interfaces_total = interfaces * 5
        elif(interfaces < 10):
            interfaces_total = interfaces * 7
        else:
            interfaces_total = interfaces * 10

        self.pf = entradas_total + salidas_total + \
            peticiones_total + archivos_total + interfaces_total

        print("PF" + str(self.pf))

        self.calcularCocomo()

    def calcularFae(self, valores):
        self.__fae = 1
        for val in valores:
            self.__fae = self.__fae * val
        print("FAE" + str(self.__fae))
        self.calcularCocomo()

