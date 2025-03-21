#AINH
import os

class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.sig = None

    def __str__(self):
        return str(self.dato) + "->" +  str(self.sig)

class Cola:
    def __init__(self,max = None):
        self.head = None
        self.tail = None
        self.size = 0
        self.max = max

    def isEmpty(self):
        return self.head == None

    def enqueue(self,dato):
        if self.isFull():
            return print("No se puede agregar a: ",dato," la cola esta llena")
        else:
            nuevo = Nodo(dato)
            self.size += 1
            if self.isEmpty():
                self.head = nuevo
                self.tail = nuevo
            else:
                self.tail.sig = nuevo
                self.tail = nuevo

    def desenque(self):
        actual = self.head
        if self.isEmpty():
            return "Empty"
        elif actual.sig == None:
            self.head = None
            self.tail = None
            self.size -= 1
            return actual.dato
        else:
            self.head = self.head.sig
            self.size -= 1
            return actual.dato

    def data(self):
        elementos = []
        if self.isEmpty():
            return "Empty"
        else:
            actual = self.head
            while actual:
                elementos.append(actual.dato)
                actual = actual.sig
            return elementos

    def posicion(self,user):
        lista = self.data()
        if self.isEmpty():
            return "Empty"
        else:
            posicion = lista.index(user) if user in lista else None
            return posicion + 1

    def peak(self):
            if self.isEmpty():
                return "Empty"
            else:
                return self.head.dato

    def isFull(self):
        return self.size == self.max

    def Original(self,calculo):
        c = calculo
        num = ""
        operadores = ["sen","cos","tan","log","ln","asen","acos","atan","e","^","*","/","+","-","(",")"]
        last_operator = True
        exp = ""
        last = ""
        for caracter in c:
            actual = caracter
            if actual not in operadores:
                if exp == "e":
                    num = num + "e"
                    exp = ""
                elif exp == "e-":
                    num = num + "e-"
                    exp = ""
                num += actual
                last_operator = False
            elif actual == "-":
                if exp == "e":
                    exp = "e-"
                elif last == ")" and last_operator:
                        self.enqueue(actual)
                        last_operator = True
                        last = actual
                elif num == "" and last_operator:
                    num += actual
                    last_operator = False
                else:
                    if num != "":
                        self.enqueue(num)
                        last = num
                        num = ""
                    self.enqueue(actual)
                    last = actual
                    last_operator = True
            elif actual == "e":
                if exp == "":
                    exp = "e"
            elif actual == "^" and exp == "e":
                self.enqueue("e^")
                last = "e^"
                exp = ""
            elif actual in operadores:
                if num != "":
                    self.enqueue(num)
                    last = num
                    num = ""
                self.enqueue(actual)
                last = actual
                last_operator = True
            else:
                if num != "":
                    self.enqueue(num)
                    last = num
                    num = ""
                last_operator = True
        if num != "":
            self.enqueue(num)
            last = num

#AINH