# -*- coding: utf-8 -*-
class Calculadora():

    def __init__(self):
        self.resultado = 0
#        self.calculo = None
#        self.num1 = 0
#        self.num2 = 0

    def sumar (self,num1,num2):
        self.resultado = num1 + num2

    def restar (self,num1,num2):
        self.resultado = num1 - num2

    def multiplicar (self,num1,num2):
        self.resultado = num1 * num2

    def dividir (self,num1,num2):
        self.resultado = num1 / num2