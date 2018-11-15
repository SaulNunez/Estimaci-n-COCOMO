import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QWidget, QPushButton, QDialogButtonBox, QLabel, QGroupBox,
                             QFormLayout, QSpinBox, QHBoxLayout, QComboBox, QListWidget, QVBoxLayout, QFileDialog, QListWidgetItem, QRadioButton, QButtonGroup, QGroupBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot, Qt
#from enum import Enum
from cocomo import Cocomo
from cocomo_model import CocomoModel


class CocomoView(QWidget):

    def __init__(self, controller):
        super(CocomoView, self).__init__()
        self.setWindowTitle('Modelo COCOMO')
        self.show()

        self.controller = controller
        self.formGroupBox = self.forma_grado_tot_influencia()
        self.forma_fae()
        self.forma_detalles_sistema()
        self.modelo_groupbox = self.crear_seleccion_modelo()
        self.tipo_groupbox = self.crear_seleccion_tipo()
        self.mainLayout = QVBoxLayout()
        self.secondary_bottom = QHBoxLayout()
        self.lenguajes_programacion_proyecto_listwidget = QListWidget()
        # self.lenguajes_programacion_proyecto_listwidget.state
        for key in Cocomo.indice_loc:
            item = QListWidgetItem(
                key, self.lenguajes_programacion_proyecto_listwidget)
            # item = QListWidgetItem()
            # item.setText(key)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            # self.lenguajes_programacion_proyecto_listwidget.addItem(item)
        self.lenguajes_programacion_proyecto_listwidget.itemChanged.connect(
            self.definir_lenguaje_programacion)
        self.secondary_bottom.addWidget(
            self.lenguajes_programacion_proyecto_listwidget)
        self.secondary_bottom.addWidget(self.formGroupBox)
        self.secondary_bottom.addWidget(self.formGroupBox2)

        self.results_group = QVBoxLayout()
        self.results_group.addWidget(QLabel("Resultados"))
        self.results_group.addWidget(QLabel("Esfuerzo (persona x mes)"))
        self.esfuerzo_label = QLabel("0")
        self.results_group.addWidget(self.esfuerzo_label)
        self.results_group.addWidget(QLabel("Tiempo de desarrollo (meses)"))
        self.tiempo_desarrollo_label = QLabel("0")
        self.results_group.addWidget(self.tiempo_desarrollo_label)
        self.results_group.addWidget(QLabel("PR(LDC/persona x mes)"))
        self.pr_label = QLabel("0")
        self.results_group.addWidget(self.pr_label)
        self.results_group.addWidget(QLabel("KLDC"))
        self.kloc_label = QLabel("0")
        self.results_group.addWidget(self.kloc_label)

        self.secondary_top = QHBoxLayout()
        self.secondary_top.addWidget(self.formGroupBox3)
        self.secondary_top.addWidget(self.modelo_groupbox)
        self.secondary_top.addWidget(self.tipo_groupbox)
        self.secondary_top.addLayout(self.results_group)

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
        formGroupBox = QGroupBox("Grado Total de Influencia")
        layout = QFormLayout()

        self.respuesta_spinbox = []

        for label in Cocomo.preguntas_grado_total_influencia:
            sb = QSpinBox()
            sb.setMinimum(0)
            sb.setMaximum(5)
            sb.valueChanged.connect(self.establecer_gti)
            layout.addRow(QLabel(label), sb)
            self.respuesta_spinbox.append(sb)

        formGroupBox.setLayout(layout)
        return formGroupBox

    def forma_fae(self):
        self.formGroupBox2 = QGroupBox("Conductores de costo")
        layout = QFormLayout()

        self.fae_combobox = {}

        for label in Cocomo.conductores_coste_fae:
            cb = QComboBox()
            for value in Cocomo.conductores_coste_fae[label]:
                cb.addItem(value)
            cb.currentIndexChanged.connect(self.establecer_valor_fae)
            # Aesthetics, hacer que la primera opción estándar para todos y más importante, sana
            index = cb.findText('Nominal', Qt.MatchFixedString)
            if index >= 0:
                cb.setCurrentIndex(index)
            layout.addRow(QLabel(label), cb)
            self.fae_combobox[label] = cb

        self.formGroupBox2.setLayout(layout)

    def modelo_seleccionado(self):
        pass

    def tipo_seleccionado(self):
        pass

    def forma_detalles_sistema(self):
        self.formGroupBox3 = QGroupBox("Datos sistema")

        layout = QFormLayout()

        self.entradas = QSpinBox()
        self.entradas.setMinimum(0)
        self.entradas.valueChanged.connect(self.cambio_datos_sistema)
        self.salidas = QSpinBox()
        self.salidas.setMinimum(0)
        self.salidas.valueChanged.connect(self.cambio_datos_sistema)
        self.peticiones = QSpinBox()
        self.peticiones.setMinimum(0)
        self.peticiones.valueChanged.connect(self.cambio_datos_sistema)
        self.archivos = QSpinBox()
        self.archivos.setMinimum(0)
        self.archivos.valueChanged.connect(self.cambio_datos_sistema)
        self.interfaces = QSpinBox()
        self.interfaces.setMinimum(0)
        self.interfaces.valueChanged.connect(self.cambio_datos_sistema)

        layout.addRow(QLabel('Entradas'), self.entradas)
        layout.addRow(QLabel('Salidas'), self.salidas)
        layout.addRow(QLabel('Peticiones'), self.peticiones)
        layout.addRow(QLabel('Archivos'), self.archivos)
        layout.addRow(QLabel('Interfaces'), self.interfaces)

        self.formGroupBox3.setLayout(layout)

    def crear_seleccion_modelo(self):
        modelo_groupbox = QGroupBox("Modelo")
        modelo_layout = QVBoxLayout()
        for label in Cocomo.Modelo:
            item = QRadioButton(label.name)
            if label == Cocomo.Modelo.BASICO:
                item.setChecked(True)
            item.toggled.connect(self.establecer_modelo)
            modelo_layout.addWidget(item)
        modelo_groupbox.setLayout(modelo_layout)
        return modelo_groupbox

    def crear_seleccion_tipo(self):
        modelo_groupbox = QGroupBox("Tipo")
        modelo_layout = QVBoxLayout()
        for label in Cocomo.Tipo:
            item = QRadioButton(label.name)
            if label == Cocomo.Tipo.ORGANICO:
                item.setChecked(True)
            item.toggled.connect(self.establecer_tipo)    
            modelo_layout.addWidget(item)
        modelo_groupbox.setLayout(modelo_layout)
        return modelo_groupbox

    @pyqtSlot(bool)
    def establecer_modelo(self, bool):
        for radio in self.modelo_groupbox.findChildren(QRadioButton):
            if radio.isChecked:
                self.controller.definir_modelo(Cocomo.Modelo[radio.text()])

    @pyqtSlot(bool)
    def establecer_tipo(self, bool):
        for radio in self.tipo_groupbox.findChildren(QRadioButton):
            if radio.isChecked:
                self.controller.definir_tipo(Cocomo.Tipo[radio.text()])

    def reset(self):
        for sp in self.respuesta_spinbox:
            sp.setValue(0)
        for comboboxes_dict in self.fae_combobox:
            index = self.fae_combobox[comboboxes_dict].findText(
                'Nominal', Qt.MatchFixedString)
            if index >= 0:
                self.fae_combobox[comboboxes_dict].setCurrentIndex(index)
        self.entradas.setValue(0)
        self.salidas.setValue(0)
        self.peticiones.setValue(0)
        self.archivos.setValue(0)
        self.interfaces.setValue(0)

        for index in range(self.lenguajes_programacion_proyecto_listwidget.count()):
            self.lenguajes_programacion_proyecto_listwidget.item(
                index).setCheckState(Qt.Unchecked)

    @pyqtSlot(int)
    def establecer_valor_fae(self, i):
        self.calculo_fae()

    @pyqtSlot(int)
    def establecer_gti(self, i):
        self.calculo_gti()

    def calculo_fae(self):
        valores = []
        for key in self.fae_combobox:
            combobox = self.fae_combobox[key]
            value = Cocomo.conductores_coste_fae[key][str(
                combobox.currentText())]
            valores.append(value)
        self.controller.fae_cambiado(valores)

    def calculo_gti(self):
        valores = []
        for sp in self.respuesta_spinbox:
            valores.append(sp.value())
        self.controller.gti_cambiado(valores)

    @pyqtSlot(int)
    def cambio_datos_sistema(self, i):
        self.calcular_pf()

    def calcular_pf(self):
        self.controller.calcularPf(self.entradas.value(), self.salidas.value(
        ), self.peticiones.value(), self.archivos.value(), self.interfaces.value())

    def salvar(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Salvar modelo actual", "", "JSON Files (*.json);;All Files (*)", options=options)
        self.controller.abrir(fileName)

    def mostrar_calculos_cocomo(self, esfuerzo, tiempo_desarrollo, personal, pr, loc):
        self.esfuerzo_label.setText(str(esfuerzo))
        self.tiempo_desarrollo_label.setText(str(tiempo_desarrollo))
        self.pr_label.setText(str(personal))
        self.kloc_label.setText(str(loc / 1000))

    def definir_lenguaje_programacion(self, item):
        lenguajes = []

        for index in range(self.lenguajes_programacion_proyecto_listwidget.count()):
            if self.lenguajes_programacion_proyecto_listwidget.item(index).checkState() == Qt.Checked:
                lenguajes.append(
                    self.lenguajes_programacion_proyecto_listwidget.item(index).text())

        self.controller.definir_lenguaje_programacion(lenguajes)

    def cambiar_tipo(self, tipo):
        pass

    def cambiar_modelo(self, modelo):
        pass

    def abrir(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Salvar modelo actual", "", "JSON Files (*.json);;All Files (*)", options=options)
        self.controller.abrir(fileName)
