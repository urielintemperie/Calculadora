# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
sys.path.append('../Controladores')
from main_controlador import *

class MainWindow (QtGui.QWidget):

    def __init__(self):
        super(MainWindow , self).__init__()
        self.controlador = MainControlador(self)
        self.init_ui()


    def escribir (self,caracter):
        self.entradaNumero.setText(caracter)


    def init_ui (self):
        grilla = QtGui.QGridLayout()
        self.entradaNumero = QtGui.QLineEdit(self)
        y_layout = QtGui.QVBoxLayout()
        y_layout.addWidget(self.entradaNumero)
        y_layout.addLayout(grilla)
        self.setLayout(y_layout)

#        soloNumeros = QtGui.QDoubleValidator(self)

#        self.entradaNumero.setValidator(soloNumeros)


        boton0 = QtGui.QPushButton('0')
        boton1 = QtGui.QPushButton('1')
        boton2 = QtGui.QPushButton('2')
        boton3 = QtGui.QPushButton('3')
        boton4 = QtGui.QPushButton('4')
        boton5 = QtGui.QPushButton('5')
        boton6 = QtGui.QPushButton('6')
        boton7 = QtGui.QPushButton('7')
        boton8 = QtGui.QPushButton('8')
        boton9 = QtGui.QPushButton('9')

        botonC = QtGui.QPushButton('C')
        botonAns = QtGui.QPushButton('Ans')
        botonBorrar = QtGui.QPushButton('<--')

        botonDividir = QtGui.QPushButton('/')
        botonMultiplicar = QtGui.QPushButton('*')
        botonRestar = QtGui.QPushButton('-')
        botonSumar = QtGui.QPushButton('+')

        botonIgual = QtGui.QPushButton('=')
        botonComa = QtGui.QPushButton(',')

        botonAbrirParentesis = QtGui.QPushButton('(')
        botonCerrarParentesis = QtGui.QPushButton(')')
#Necesito hacer este proceso para poder lograr que en los botones es x² y √, dado que por el tipo de codificacion no los comprende, a menos que lo decodifique manualmente especificando que sea utf-8 que si conoce estos caracteres
        s1 = "x²"
        d1 = s1.decode('utf-8')
        botonAlCuadrado = QtGui.QPushButton(d1)
        s2 = "√"
        d2 = s2.decode('utf-8')
        botonRaizCuadrada = QtGui.QPushButton(d2)
        botonLogaritmo = QtGui.QPushButton('log')


        grilla.addWidget(botonC,0,0)
        grilla.addWidget(botonAns,0,1)
        grilla.addWidget(botonBorrar,0,2)

        grilla.addWidget(boton0,4,0)
        grilla.addWidget(boton1,3,0)
        grilla.addWidget(boton2,3,1)
        grilla.addWidget(boton3,3,2)
        grilla.addWidget(boton4,2,0)
        grilla.addWidget(boton5,2,1)
        grilla.addWidget(boton6,2,2)
        grilla.addWidget(boton7,1,0)
        grilla.addWidget(boton8,1,1)
        grilla.addWidget(boton9,1,2)

        grilla.addWidget(botonDividir,3,4)
        grilla.addWidget(botonMultiplicar,4,4)
        grilla.addWidget(botonRestar,3,3)
        grilla.addWidget(botonSumar,4,3)

        grilla.addWidget(botonIgual,4,2)
        grilla.addWidget(botonComa,4,1)

        grilla.addWidget(botonAlCuadrado,2,3)
        grilla.addWidget(botonRaizCuadrada,2,4)
        grilla.addWidget(botonAbrirParentesis,1,3)
        grilla.addWidget(botonCerrarParentesis,1,4)
        grilla.addWidget(botonLogaritmo,1,5)


        boton0.clicked.connect(lambda: self.controlador.escribir('0'))
        boton1.clicked.connect(lambda: self.controlador.escribir('1'))
        boton2.clicked.connect(lambda: self.controlador.escribir('2'))
        boton3.clicked.connect(lambda: self.controlador.escribir('3'))
        boton4.clicked.connect(lambda: self.controlador.escribir('4'))
        boton5.clicked.connect(lambda: self.controlador.escribir('5'))
        boton6.clicked.connect(lambda: self.controlador.escribir('6'))
        boton7.clicked.connect(lambda: self.controlador.escribir('7'))
        boton8.clicked.connect(lambda: self.controlador.escribir('8'))
        boton9.clicked.connect(lambda: self.controlador.escribir('9'))

        botonRestar.clicked.connect(lambda: self.controlador.handler_botonMenos())
        botonSumar.clicked.connect(lambda: self.controlador.handler_botonMas())
        botonMultiplicar.clicked.connect(lambda: self.controlador.handler_botonMultiplicar())
        botonDividir.clicked.connect(lambda: self.controlador.handler_botonDividir())
        botonComa.clicked.connect(lambda: self.controlador.handler_botonComa())
        botonIgual.clicked.connect(lambda: self.controlador.handler_igual())

        botonAns.clicked.connect(lambda: self.controlador.handler_botonAns())
        botonC.clicked.connect(lambda: self.controlador.handler_botonC())
#        botonC.clicked.connect(self.controlador.)
        botonBorrar.clicked.connect(lambda: self.controlador.handler_botonBorrar())

        botonAbrirParentesis.clicked.connect(lambda: self.controlador.escribir('('))#handler_botonAbrirParentesis)
        botonCerrarParentesis.clicked.connect(lambda: self.controlador.escribir(')'))#handler_botonCerrarParentesis)
        botonRaizCuadrada.clicked.connect(lambda: self.controlador.handler_botonRaizCuadrada)
        botonAlCuadrado.clicked.connect(lambda: self.controlador.handler_botonAlCuadrado)
        botonLogaritmo.clicked.connect(lambda: self.controlador.escribir('log'))#handler_botonLogaritmo)



        '''
        names = ['C','Ans','','',
                '7','8','9','/',
                '4','5','6','x',
                '1','2','3','-',
                '0','.','=','+']

        positions = [(i,j) for i in range(5) for j in range (4)]

        for position, name in zip(positions,names):
            if name == '':
                continue
            button = QtGui.QPushButton(name)
#            print button.objectName()
#            if name == ('0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9'):
            button.clicked.connect(lambda: self.escribir(button.objectName()))
            grilla.addWidget(button, *position)

#        button.clicked.connect(lambda: self.escribir('2'))
        '''

        self.move(300,300)
        self.setWindowTitle('calculadora')
        self.show()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())