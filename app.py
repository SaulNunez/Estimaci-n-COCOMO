import sys
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QPushButton, QDialogButtonBox, QLabel, QGroupBox, QFormLayout, QSpinBox, QHBoxLayout, QComboBox, QListWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from enum import Enum
from cocomo import Cocomo
from cocomo_model import CocomoModel


class App(QWidget):

    def __init__(self):
        super(App, self).__init__()
        self.setWindowTitle('Método COCOMO')
        self.show()

        self.forma_grado_tot_influencia()
        self.forma_fae()
        self.forma_detalles_sistema()
        self.mainLayout = QHBoxLayout()
        self.lenguajes_programacion_proyecto_listwidget = QListWidget()
        #self.lenguajes_programacion_proyecto_listwidget.state
        for key in Cocomo.indice_loc:
            self.lenguajes_programacion_proyecto_listwidget.addItem(key)
        self.mainLayout.addWidget(self.lenguajes_programacion_proyecto_listwidget)
        self.mainLayout.addWidget(self.formGroupBox)
        self.mainLayout.addWidget(self.formGroupBox2)
        self.mainLayout.addWidget(self.formGroupBox3)
        self.setLayout(self.mainLayout)

    def forma_grado_tot_influencia(self):
        self.formGroupBox = QGroupBox("Grado Total de Influencia")
        layout = QFormLayout()

        self.respuesta_spinbox = []

        for label in Cocomo.preguntas_grado_total_influencia:
            sb = QSpinBox()
            sb.setMinimum(0)
            sb.setMaximum(5)
            layout.addRow(QLabel(label), sb)
            self.respuesta_spinbox.append(sb) 

        self.formGroupBox.setLayout(layout)

    def forma_fae(self):
        self.formGroupBox2 = QGroupBox("Variable FAE")
        layout = QFormLayout()

        self.fae_combobox =[]

        for label in Cocomo.variables_fae:
            cb = QComboBox()
            for value in Cocomo.variables_fae[label]:
                cb.addItem(value)
            # Aesthetics, hacer que la primera opción estándar para todos y más importante, sana
            index = cb.findText('Nominal', Qt.MatchFixedString)
            if index >= 0:
                cb.setCurrentIndex(index)
            layout.addRow(QLabel(label), cb)
            self.fae_combobox.append(cb) 

        self.formGroupBox2.setLayout(layout)

    def forma_detalles_sistema(self):
        self.formGroupBox3 = QGroupBox("Datos sistema")

        layout = QFormLayout()

        entradas = QSpinBox()
        entradas.setMinimum(0)
        salidas = QSpinBox()
        salidas.setMinimum(0)
        peticiones = QSpinBox()
        peticiones.setMinimum(0)
        archivos = QSpinBox()
        archivos.setMinimum(0)
        interfaces = QSpinBox()
        interfaces.setMinimum(0)

        layout.addRow(QLabel('Entradas'), entradas)
        layout.addRow(QLabel('Salidas'), salidas)
        layout.addRow(QLabel('Peticiones'), peticiones)
        layout.addRow(QLabel('Archivos'), archivos)
        layout.addRow(QLabel('Interfaces'), interfaces)

        self.formGroupBox3.setLayout(layout)

        def reset(self):
            pass
        def calculo_fae(self):
            pass
        def calculo_gti(self):
            pass
        def calcular_cocomo(self):
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
