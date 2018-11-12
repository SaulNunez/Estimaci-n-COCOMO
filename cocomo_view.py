import sys
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QPushButton, QDialogButtonBox, QLabel, QGroupBox, QFormLayout, QSpinBox, QHBoxLayout, QComboBox, QListWidget, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
#from enum import Enum
from cocomo import Cocomo
from cocomo_model import CocomoModel

class CocomoView(QWidget):

    def __init__(self):
        super(CocomoView, self).__init__()
        self.setWindowTitle('Modelo COCOMO')
        self.show()

        self.forma_grado_tot_influencia()
        self.forma_fae()
        self.forma_detalles_sistema()
        self.mainLayout = QVBoxLayout()
        self.secondary_bottom = QHBoxLayout()
        self.lenguajes_programacion_proyecto_listwidget = QListWidget()
        #self.lenguajes_programacion_proyecto_listwidget.state
        for key in Cocomo.indice_loc:
            self.lenguajes_programacion_proyecto_listwidget.addItem(key)
        self.secondary_bottom.addWidget(self.lenguajes_programacion_proyecto_listwidget)
        self.secondary_bottom.addWidget(self.formGroupBox)
        self.secondary_bottom.addWidget(self.formGroupBox2)

        self.secondary_top = QHBoxLayout()
        self.secondary_top.addWidget(self.formGroupBox3)

        self.mainLayout.addLayout(self.secondary_top)
        self.mainLayout.addLayout(self.secondary_bottom)

        self.button_row = QHBoxLayout()
        self.reset_button = QPushButton("Reestablecer", self)
        self.reset_button.clicked.connect(self.reset)
        self.button_row.addWidget(self.reset_button)
        self.load_button = QPushButton("Cargar", self)
        self.load_button.clicked.connect(self.abrir)
        self.button_row.addWidget(self.load_button)
        self.save_button = QPushButton("Salvar", self)
        self.save_button.clicked.connect(self.salvar)
        self.button_row.addWidget(self.save_button)
        self.mainLayout.addLayout(self.button_row)
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

        for label in Cocomo.conductores_coste_fae:
            cb = QComboBox()
            for value in Cocomo.conductores_coste_fae[label]:
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

        self.entradas = QSpinBox()
        self.entradas.setMinimum(0)
        self.salidas = QSpinBox()
        self.salidas.setMinimum(0)
        self.peticiones = QSpinBox()
        self.peticiones.setMinimum(0)
        self.archivos = QSpinBox()
        self.archivos.setMinimum(0)
        self.interfaces = QSpinBox()
        self.interfaces.setMinimum(0)

        layout.addRow(QLabel('Entradas'), self.entradas)
        layout.addRow(QLabel('Salidas'), self.salidas)
        layout.addRow(QLabel('Peticiones'), self.peticiones)
        layout.addRow(QLabel('Archivos'), self.archivos)
        layout.addRow(QLabel('Interfaces'), self.interfaces)

        self.formGroupBox3.setLayout(layout)

    def reset(self):
        for sp in self.respuesta_spinbox:
            sp.setValue(0)
        for cb in self.fae_combobox:
            index = cb.findText('Nominal', Qt.MatchFixedString)
            if index >= 0:
                cb.setCurrentIndex(index)
        self.entradas.setValue(0)
        self.salidas.setValue(0)
        self.peticiones.setValue(0)
        self.archivos.setValue(0)
        self.interfaces.setValue(0)
        
    def calculo_fae(self):
        pass
    def calculo_gti(self):
        pass
    def calcular_cocomo(self):
        pass

    def salvar(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,"Salvar modelo actual","","JSON Files (*.json);;All Files (*)", options=options)

    def abrir(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"Abrir modelo existente","","JSON Files (*.json);;All Files (*)", options=options)
