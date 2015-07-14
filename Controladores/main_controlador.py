# -*- coding: utf-8 -*-
import sys
sys.path.append('../Modelo')
from calculadora import *


class MainControlador():

    def __init__(self, una_ventana):
        self.calculadora = Calculadora()
        self.ventana = una_ventana
        self.posicion = 0
#        self.calculo = None

    def handler_sumar (self,posicion):
        '''
#        self.ventana.entradaNumero.setSelection(self.posicion,self.ventana.entradaNumero.cursorPosition())
        self.calculadora.num1 = int ((self.ventana.entradaNumero.text())[self.posicion:self.ventana.entradaNumero.cursorPosition()])
#        self.calculadora.num1 = int (self.ventana.entradaNumero.selectedText())
        self.escribir('+')
        self.calculadora.calculo = self.calculadora.sumar
        self.posicion = self.ventana.entradaNumero.cursorPosition()
        print self.posicion
#        self.sumar(num1,num2)
#        self.actualizar_qlineedit()
        '''
        numero1 = self.calculo[self.buscarIzquierda(posicion):posicion]
        print "(sumar) numero 1:"
        print numero1
        numero2 = self.calculo[(posicion+1):self.buscarDerecha(posicion)]
        print "(sumar) numero 2:"
        print numero2
        self.calculadora.sumar(int(numero1),int(numero2))
        resultado = self.calculadora.resultado
        print "(sumar) resultado:"
        print resultado
        print "(sumar) tipo de self.calculo:"
        print type (self.calculo)
        self.calculo = self.modificarString(self.calculo,self.buscarIzquierda(posicion),(self.buscarDerecha(posicion)-1),str(resultado))
        print "(sumcar) calculo:"
        print self.calculo

    def handler_restar (self,posicion):
#        self.calculo
#        self.resta(num1,num2)
#        self.actualizar_qlineedit()
        numero1 = self.calculo[self.buscarIzquierda(posicion):posicion]
        print "(sumar) numero 1:"
        print numero1
        numero2 = self.calculo[(posicion+1):self.buscarDerecha(posicion)]
        print "(sumar) numero 2:"
        print numero2
        self.calculadora.restar(int(numero1),int(numero2))
        resultado = self.calculadora.resultado
        print "(sumar) resultado:"
        print resultado
        print "(sumar) tipo de self.calculo:"
        print type (self.calculo)
        self.calculo = self.modificarString(self.calculo,self.buscarIzquierda(posicion),(self.buscarDerecha(posicion)-1),str(resultado))
        print "(sumcar) calculo:"
        print self.calculo



    def handler_multiplicar (self,posicion):
#        self.multiplicar(num1,num2)
#        self.actualizar.qlineedit()
        numero1 = self.calculo[self.buscarIzquierda(posicion):posicion]
        print "(restar) numero 1:"
        print numero1
        numero2 = self.calculo[(posicion+1):self.buscarDerecha(posicion)]
        print "(restar) numero 2:"
        print numero2
        self.calculadora.multiplicar(int(numero1),int(numero2))
        resultado = self.calculadora.resultado
#        self.calculo[self.buscarIzquierda(posicion)] = resultado
        print "(restar) resultado:"
        print resultado
        print "(restar) tipo de self.calculo:"
        print type (self.calculo)
#los string en python son inmutables, por lo que no se puede modificar lo que tienen dentro como se haria con una lista
#        prueba = "hola"
#        print prueba
#        print len(prueba)
#        prueba [1:3] = 'p'
#        prueba = self.modificarString(prueba,1,2,'pablo')
#        print prueba
        self.calculo = self.modificarString(self.calculo,self.buscarIzquierda(posicion),(self.buscarDerecha(posicion)-1),str(resultado))
#        self.calculo[self.buscarIzquierda(posicion):self.buscarDerecha(posicion)] =  resultado
#        self.calculo[(self.buscarIzquierda(posicion) + 1):self.buscarDerecha(posicion)]=str(resultado)
        print "(multiplicar) calculo:"
        print self.calculo


    def handler_dividir (self,posicion):
#        numero1 = self.calculo[self.buscarIzquierda(posicion):posicion]
#        numero2 = self.calculo[posicion:self.buscarDerecha(posicion)]
#        self.calculadora.dividir()
#        self.dividir(num1,num2)
#        self.actualizar_qlineedit()

        numero1 = self.calculo[self.buscarIzquierda(posicion):posicion]
        print "(dividir) numero 1:"
        print numero1
        numero2 = self.calculo[(posicion+1):self.buscarDerecha(posicion)]
        print "(dividir) numero 2:"
        print numero2
        self.calculadora.dividir(int(numero1),int(numero2))
        resultado = self.calculadora.resultado
#        self.calculo[self.buscarIzquierda(posicion)] = resultado
        print "(dividir) resultado:"
        print resultado
        print "(dividir) tipo de self.calculo:"
        print type (self.calculo)
#los string en python son inmutables, por lo que no se puede modificar lo que tienen dentro como se haria con una lista
#        prueba = "hola"
#        print prueba
#        print len(prueba)
#        prueba [1:3] = 'p'
#        prueba = self.modificarString(prueba,1,2,'pablo')
#        print prueba
        self.calculo = self.modificarString(self.calculo,self.buscarIzquierda(posicion),(self.buscarDerecha(posicion)-1),str(resultado))
        print "(dividir) calculo:"
        print self.calculo

    def handler_igual (self):
        '''
        self.ventana.entradaNumero.setSelection(0,self.posicion)
        self.ventana.entradaNumero.cut()
        self.calculadora.num2 = int (self.ventana.entradaNumero.text())
        self.calculadora.sumar()
        self.ventana.entradaNumero.paste()
        self.ventana.entradaNumero.setCursorPosition((self.ventana.entradaNumero.text()).length())
        self.escribir('=')
        self.escribir(str(self.calculadora.resultado))
        '''

#        self.calculo = self.ventana.entradaNumero.text()
        self.calculo = str(self.ventana.entradaNumero.text())
        print "calculo original:"
        print self.calculo

        posicion = 0
        multiplicaciones = []
        divisiones = []
        sumas = []
        restas = []
        for caracter in self.calculo:
            if caracter == '*':
                multiplicaciones = multiplicaciones + [posicion]
            if caracter == '/':
                divisiones = divisiones + [posicion]
            if caracter == '+':
                sumas = sumas + [posicion]
            if caracter == '-':
                restas = restas + [posicion]
            posicion += 1
#        print self.calculo.find('*')
        print "multiplicaciones:"
        print multiplicaciones
        print "divisiones:"
        print divisiones
        print "sumas:"
        print sumas
        print "restas:"
        print restas


        for multiplicacion in multiplicaciones:
            posicion = 0
            multiplicaciones2 = []
            for caracter in self.calculo:
                if caracter == '*':
                    multiplicaciones2 = multiplicaciones2 + [posicion]
                posicion +=1
            print "multiplicaciones 2:"
            print multiplicaciones2
            print "multiplicaciones 2 [0]:"
            print multiplicaciones2[0]
            self.handler_multiplicar(multiplicaciones2[0])
        for division in divisiones:
            posicion = 0
            divisiones2 = []
            for caracter in self.calculo:
                if caracter == '/':
                    divisiones2 = divisiones2 + [posicion]
                posicion +=1
            print "divisiones 2:"
            print divisiones2
            self.handler_dividir(divisiones2[0])
#            self.handler_dividir(division)
        for suma in sumas:
            posicion = 0
            sumas2 = []
            for caracter in self.calculo:
                if caracter == '+':
                    sumas2 = sumas2 + [posicion]
                posicion +=1
            print "sumas 2:"
            print sumas2
            self.handler_sumar(sumas2[0])
        for resta in restas:
            posicion = 0
            restas2 = []
            for caracter in self.calculo:
                if caracter == '-':
                    restas2 = restas2 + [posicion]
                posicion +=1
            print "restas 2:"
            print restas2
            self.handler_restar(restas2[0])

        print "ultima impresion calculo:"
        print self.calculo
#        self.handler_multiplicar
        self.handler_botonC()
        self.escribir(self.calculo)


    def handler_botonMas (self):
        self.escribir('+')

    def handler_botonMenos (self):
        self.escribir('-')

    def handler_botonMultiplicar (self):
        self.escribir('*')

    def handler_botonDividir (self):
        self.escribir('/')

    def handler_botonC (self):
        self.ventana.entradaNumero.clear()

    def handler_botonAns (self):
        self.escribir(self.calculo)

    def handler_botonBorrar (self):
        if len(str(self.ventana.entradaNumero.text()))>= 3 :

#            self.ventana.entradaNumero.setSelection(self.ventana.entradaNumero.cursorPosition(),((self.ventana.entradaNumero.cursorPosition())-3))
            self.ventana.entradaNumero.setSelection(((self.ventana.entradaNumero.cursorPosition())-3),self.ventana.entradaNumero.cursorPosition())
#            print self.ventana.entradaNumero.selectedText()
            if self.ventana.entradaNumero.selectedText() == 'log':
                self.ventana.entradaNumero.del_()
            else:
                self.ventana.entradaNumero.deselect()
                self.ventana.entradaNumero.backspace()
        else:
            self.ventana.entradaNumero.backspace()
#        self.ventana.entradaNumero.undo()
#        self.ventana.entradaNumero.cursorWordBackward('log')
#        self.ventana.entradaNumero.del_()
#        self.ventana.entradaNumero.backspace()

    def handler_botonComa (self):
        self.escribir(',')

    def handler_botonAbrirParentesis(self):
        self.escribir('(')

    def handler_botonCerrarParentesis(self):
        self.escribir(')')

    def handler_botonRaizCuadrada(self):
        s = "√"
        d = s.decode('utf-8')
        self.escribir(d)

    def handler_botonAlCuadrado(self):
        s = "x²"
        d = s.decode('utf-8')
        self.escribir(d)

    def handler_botonLogaritmo(self):
        self.escricribir('log')

    def buscarIzquierda (self,inicio):
        i = 0
        contador = 1
        resultado = 0
        while (i != 1) and (inicio - contador >= 0) :
            if (self.calculo[(inicio - contador)] == '+') or (self.calculo[(inicio - contador)] == '-') or (self.calculo[(inicio - contador)] == '*') or (self.calculo[(inicio - contador)] == '/'):
                i = 1
                resultado = inicio - (contador - 1)
                return resultado
            contador +=1

    def buscarDerecha (self,iniciobase):
        i = 0
        contador = 0
        resultado = 0
        inicio = iniciobase + 1
#        while (i != 1) and (inicio + contador <= (self.calculo.length() - 1)) :
        while (i != 1) and (inicio + contador <= (len(self.calculo) - 1)) :
            if (self.calculo[inicio + contador] == '+') or (self.calculo[inicio + contador] == '-') or (self.calculo[inicio + contador] == '*') or (self.calculo[inicio + contador] == '/'):
                i = 1
                resultado = inicio + contador
                return resultado
            contador +=1
        if i == 0:
#            return self.calculo.length()
            return len(self.calculo)



#    def modificarString (self,stringOriginal,inicio,fin,añadido):
#Me saltaba invalid sintax porque NO RECONOCE LA Ñ
    def modificarString (self,stringOriginal,inicio,fin,agregar):
        intermedio = ""
        contador = 0
        yaAgregado = 0
        for caracter in stringOriginal:
            if (contador < inicio) or (contador > fin):
                intermedio = intermedio + caracter
            else:
                if yaAgregado == 0:
                    intermedio = intermedio + agregar
                    yaAgregado = 1
#                intermedio = intermedio + añadido
#NO RECONOCE LA Ñ
            contador +=1
#        stringOriginal = intermedio
        return intermedio

    def escribir (self,caracter):
        self.ventana.entradaNumero.insert(caracter)

    def actualizar_qlineedit (self):
        self.ventana.entradaNumero.insert(str(self.calculadora.resultado))

