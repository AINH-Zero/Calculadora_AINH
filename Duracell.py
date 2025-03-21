#AINH
import os
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.sig = None

    def __str__(self):
        return str(self.dato) + "->" +  str(self.sig)

class Pila:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.sig = self.head
        self.head = nuevo
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "None"
        else:
            actual = self.head.dato
            self.head = self.head.sig
            self.size -= 1
            return actual

    def top(self):
        if self.isEmpty():
            return "None"
        else:
            return self.head.dato

class Nodo_operadores:
    def __init__(self,dato):
        self.dato = dato
        self.sig = None

    def __str__(self):
        return str(self.dato) + "->" +  str(self.sig)

class Operadores:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def push(self, dato):
        nuevo = Nodo_operadores(dato)
        nuevo.sig = self.head
        self.head = nuevo
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "None"
        else:
            actual = self.head.dato
            self.head = self.head.sig
            self.size -= 1
            return actual

    def top(self):
        if self.isEmpty():
            return "None"
        else:
            return self.head.dato

#AINH