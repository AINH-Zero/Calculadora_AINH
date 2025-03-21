#AINH
import math
import Duracell
pila = Duracell.Pila()
Operadores = Duracell.Operadores()

def pos2val (posfix):
    operadores = ["sen","cos","tan","log","ln","asen","acos","atan","e^","^","*","/","+","-"]
    p = posfix.split()
    for i in range (len(p)):
        actual = p[i]
        oper = False
        for j in operadores:
            if j == actual:
                oper = True
        if oper != True:
            try:
                pila.push(float(actual))
            except ValueError:
                return "Syntax Error: Elemento no valido " + actual
        elif actual == "sen" or actual == "cos" or actual == "tan" or actual == "log" or actual == "ln" or actual == "asen" or actual == "acos" or actual == "atan" or actual == "e^":
            try:
                A = float(pila.pop())
                if actual == "sen":
                    A = math.radians(A)
                    C = math.sin(A)
                elif actual == "cos":
                    A = math.radians(A)
                    C = math.cos(A)
                elif actual == "tan":
                    A = math.radians(A)
                    C = math.tan(A)
                elif actual == "log":
                    if A <= 0:
                        return "Math Error: Logaritmo"
                    C = math.log10(A)
                elif actual == "ln":
                    if A <= 0:
                        return "Math Error: Logaritmo"
                    C = math.log(A)
                elif actual == "asen":
                    A = math.asin(A)
                    C = math.degrees(A)
                elif actual == "acos":
                    A = math.acos(A)
                    C = math.degrees(A)
                elif actual == "atan":
                    A = math.atan(A)
                    C = math.degrees(A)
                elif actual == "e^":
                    C = math.pow(math.e,A)
                pila.push(C)
            except IndexError:
                return "Sintax Error: Pila vacía"
            except ValueError:
                return "Sintax Error: Valor inválido para función"
            except Exception as e:
                return "Error: " + str(e)
        else:
            try:
                B = float(pila.pop())
                A = float(pila.pop())
                if actual == "^":
                    C = pow(A,B)
                elif actual == "*":
                    C = A * B
                elif actual == "/":
                    C = A / B
                elif actual == "+":
                    C = A + B
                elif actual == "-":
                    C = A - B
                pila.push(C)
            except IndexError:
                return "Syntax Error: Pila vacía"
            except ZeroDivisionError:
                return "Math Error: División por cero"
            except Exception as e:
                return "Error: " + str(e)
        oper = False
    if pila.size != 1:
        return "Syntax Error: Expresión postfix inválida."
    return pila.pop()

#AINH