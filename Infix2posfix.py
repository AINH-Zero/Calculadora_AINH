#AINH
import Duracell
Operadores = Duracell.Operadores()

def infix2pos (infix):
    o = Operadores
    oper = ["(",")","sen","cos","tan","log","ln","asen","acos","atan","e^","^","*","/","+","-"]
    jerarquia = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "sen": 4, "cos": 4, "tan": 4, "log": 4, "ln": 4, "asen": 4, "acos": 4, "atan": 4, "e^": 4}
    inf = infix.split()
    posfix = ""
    parentesis = 0
    for i in range (len(inf)):
        actual = inf[i]
        ec = False
        for j in oper:
            if j == actual:
                ec = True
        if ec != True:
            posfix += actual + " "
        elif actual == "(":
            o.push(actual)
            parentesis += 1
        elif actual == ")":
            parentesis -= 1
            if parentesis < 0:
                return "Parentesis"
            while o.top() != "(":
                posfix += o.pop() + " "
            if o.isEmpty():
                return "Parentesis"
            o.pop()
        else:
            while not o.isEmpty() and jerarquia.get(o.top(), -1) >= jerarquia.get(actual, -1) and o.top() != "(":
                posfix += o.pop() + " "
            o.push(actual)
        ec = False
    if parentesis != 0:
        return "Parentesis"
    while o.isEmpty() != True:
        if o.top() == "(":
            return "Parentesis"
        posfix += o.pop() + " "
    return posfix

#AINH