#AINH
import tkinter as tk
import Infix2posfix
import Posfix2Value
import Tails
infix2pos = Infix2posfix.infix2pos
pos2val = Posfix2Value.pos2val
tail = Tails.Cola()

class Calculadora:
    def __init__(self, mcr):
        #self.sqr = 0
        self.mcr = mcr
        self.time = False
        self.mcr.title("Calculator Zero_AINH")
        self.mcr.configure(bg="#E0F7FA") 

        self.pantalla = tk.Entry(mcr, width=110, borderwidth=10, bg="#B2EBF2", fg="#004D40")
        self.pantalla.grid(row=0, column=0, columnspan=15, padx=10, pady=10)

        Watermark = tk.Label(mcr, text="Zero_AINH", bg="#E0F7FA", fg="#004D40").grid(row=7, column=7, padx=5, pady=5)

        numeros = tk.Label(mcr, text="Numbers", bg="#E1F7FC", fg="#114D41").grid(row=1, column=1)
        self.B7 = tk.Button(self.mcr, text="7", command=lambda: self.click_boton("7"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=0)
        self.B8 = tk.Button(self.mcr, text="8", command=lambda: self.click_boton("8"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=1)
        self.B9 = tk.Button(self.mcr, text="9", command=lambda: self.click_boton("9"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=2)
        self.B4 = tk.Button(self.mcr, text="4", command=lambda: self.click_boton("4"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=3, column=0)
        self.B5 = tk.Button(self.mcr, text="5", command=lambda: self.click_boton("5"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=3, column=1)
        self.B6 = tk.Button(self.mcr, text="6", command=lambda: self.click_boton("6"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=3, column=2)
        self.B1 = tk.Button(self.mcr, text="1", command=lambda: self.click_boton("1"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=4, column=0)
        self.B2 = tk.Button(self.mcr, text="2", command=lambda: self.click_boton("2"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=4, column=1)
        self.B3 = tk.Button(self.mcr, text="3", command=lambda: self.click_boton("3"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=4, column=2)
        self.B0 = tk.Button(self.mcr, text="0", command=lambda: self.click_boton("0"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=5, column=1)

        OperacionesB = tk.Label(mcr, text="Math", bg="#E1F7FC", fg="#114D41").grid(row=1, column=4)
        self.BM = tk.Button(self.mcr, text="+", command=lambda: self.click_boton("+"), padx=20, pady=20, bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=3)
        self.BR = tk.Button(self.mcr, text="-", command=lambda: self.click_boton("-"), padx=21, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=4)
        self.BX = tk.Button(self.mcr, text="*", command=lambda: self.click_boton("*"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=5)
        self.BD = tk.Button(self.mcr, text="/", command=lambda: self.click_boton("/"), padx=21, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=3, column=4)

        OperacionesF = tk.Label(mcr, text="Functions", bg="#E1F7FC", fg="#114D41").grid(row=1, column=7)
        self.BS = tk.Button(self.mcr, text="sen", command=lambda: self.click_boton("sen"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=6)
        self.BC = tk.Button(self.mcr, text="cos", command=lambda: self.click_boton("cos"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=7)
        self.BT = tk.Button(self.mcr, text="tan", command=lambda: self.click_boton("tan"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=8)
        self.BL = tk.Button(self.mcr, text="log", command=lambda: self.click_boton("log"), padx=22, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=3, column=6)
        self.BLN = tk.Button(self.mcr, text="ln", command=lambda: self.click_boton("ln"), padx=25, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=3, column=7)
        self.BAS = tk.Button(self.mcr, text="asen", command=lambda: self.click_boton("asen"), padx=15, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=3, column=8)
        self.BAC = tk.Button(self.mcr, text="acos", command=lambda: self.click_boton("acos"), padx=16, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=4, column=6)
        self.BAT = tk.Button(self.mcr, text="atan", command=lambda: self.click_boton("atan"), padx=17, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=4, column=7)
        self.BAL = tk.Button(self.mcr, text="10^n", command=lambda: self.click_boton("alog"), padx=16, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=4, column=8)
        self.BALN = tk.Button(self.mcr, text="e^n", command=lambda: self.click_boton("aln"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=5, column=7)

        OperacionesS = tk.Label(mcr, text="Specials", bg="#E1F7FC", fg="#114D41").grid(row=1, column=10)
        self.BP1 = tk.Button(self.mcr, text="(", command=lambda: self.click_boton("("), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=9)
        self.BP2 = tk.Button(self.mcr, text=")", command=lambda: self.click_boton(")"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=10)
        self.BR = tk.Button(self.mcr, text="sqr", command=lambda: self.click_boton("sqr"), padx=15, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=11)
        self.BPO = tk.Button(self.mcr, text="^", command=lambda: self.click_boton("^"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=3, column=10)

        OperacionesF = tk.Label(mcr, text="Utilities", bg="#E1F7FC", fg="#114D41").grid(row=1, column=13)
        self.BP = tk.Button(self.mcr, text=".", command=lambda: self.click_boton("."), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=12)
        self.BAC = tk.Button(self.mcr, text="AC", command=lambda: self.click_boton("AC"), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=13)
        self.BI = tk.Button(self.mcr, text="=", command=lambda: self.click_boton("="), padx=20, pady=20 , bg="#B2DFDB", activebackground="#80CBC4").grid(row=2, column=14)

        Eggs = tk.Label(mcr, text="No tocar", bg="#E1F7FC", fg="#114D41").grid(row=1, column=16)
        self.BP = tk.Button(self.mcr, text="No tocar", command=lambda: self.click_boton("destruccion"), padx=8, pady=20 , bg="red", fg="white", activebackground="#80CBC4").grid(row=2, column=15)
        self.BPE = tk.Button(self.mcr, text="Pera", command=lambda: self.click_boton("Pera"), padx=19, pady=20, bg="#98FB98", fg="black", activebackground="#80CBC4").grid(row=2, column=16)

        self.Infi = tk.Label(mcr, text="Infix: ", bg="#E0F7FA", fg="#004D40")
        self.Infi.grid(row=3, column=16, padx=5, pady=5)
        self.Posfi = tk.Label(mcr, text="Posfix: ", bg="#E0F7FA", fg="#004D40")
        self.Posfi.grid(row=4, column=16, padx=5, pady=5)

    def click_boton(self, elemento):
        ["sen","cos","tan","log","ln","asen","acos","atan","alog","aln","sqr"]
        if self.time == False:
            if elemento == "destruccion":
                self.time = True
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, "Que triste")
                self.mcr.after(2000, lambda: self.pantalla.delete(0, tk.END))
                self.mcr.after(2000, lambda: self.pantalla.insert(tk.END,"Fue decirnos adiós"))
                self.mcr.after(4000, lambda: self.pantalla.delete(0, tk.END))
                self.mcr.after(4000, lambda: self.pantalla.insert(tk.END,"Cuando nos adorábamos más"))
                self.mcr.after(6000, lambda: self.pantalla.delete(0, tk.END))
                self.mcr.after(6000, lambda: self.pantalla.insert(tk.END,"Hasta la golondrina emigró"))
                self.mcr.after(8000, lambda: self.pantalla.delete(0, tk.END))
                self.mcr.after(8000, lambda: self.pantalla.insert(tk.END,"Presagiando el final"))
                self.mcr.after(10000, self.mcr.quit)
            elif elemento == "Pera":
                self.time = True
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, "Pera")
                self.mcr.after(1000, lambda: self.pantalla.delete(0, tk.END))
                self.mcr.after(1000, lambda: self.pantalla.insert(tk.END,"Espera"))
                self.mcr.after(3000, lambda: self.pantalla.delete(0, tk.END))
                self.mcr.after(3000, lambda: self.pantalla.insert(tk.END,"Aún la nave del olvido no ha partido"))
                self.mcr.after(6000, lambda: self.pantalla.delete(0, tk.END))
                self.mcr.after(6000, lambda: self.pantalla.insert(tk.END,"No condenemos al naufragio lo vivido"))
                self.mcr.after(9000, lambda: self.pantalla.delete(0, tk.END))
                self.mcr.after(9000, lambda: self.pantalla.insert(tk.END,"Por nuestro ayer, por nuestro amor, yo te lo pido"))
                self.mcr.after(12000, lambda: self.pantalla.delete(0, tk.END))
                self.mcr.after(12000, lambda: self.pantalla.insert(tk.END,"Espera un poco!!!!!"))
                self.mcr.after(15000, lambda: self.pantalla.delete(0, tk.END))
                self.mcr.after(15000, lambda: self.pantalla.insert(tk.END,"Un poquito más"))
                self.mcr.after(18000, lambda: self.pantalla.delete(0, tk.END))
                self.mcr.after(18000, lambda: self.pantalla.insert(tk.END,"Para llevarte mi felicidad"))
                self.mcr.after(21000, self.mcr.quit)
            elif elemento == "sen":
                self.pantalla.insert(tk.END, "sen(")
            elif elemento == "cos":
                self.pantalla.insert(tk.END, "cos(")
            elif elemento == "tan":
                self.pantalla.insert(tk.END, "tan(")
            elif elemento == "log":
                self.pantalla.insert(tk.END, "log(")
            elif elemento == "ln":
                self.pantalla.insert(tk.END, "ln(")
            elif elemento == "asen":
                self.pantalla.insert(tk.END, "asen(")
            elif elemento == "acos":
                self.pantalla.insert(tk.END, "acos(")
                tail.enqueue("acos" + " ")
            elif elemento == "atan":
                self.pantalla.insert(tk.END, "atan(")
            elif elemento == "alog":
                self.pantalla.insert(tk.END, "10^")
            elif elemento == "aln":
                self.pantalla.insert(tk.END, "e^")
            elif elemento == "sqr":
                self.pantalla.insert(tk.END, "^0.5")
            elif elemento == "AC":
                    self.pantalla.delete(0, tk.END)
                    while tail.isEmpty() == False:
                        tail.desenque()
            elif elemento == "=":
                preinfix = ""
                control = True
                data = self.pantalla.get()
                if data == "":
                    pass
                else:
                    for caracter in data:
                        if caracter != " ":
                            preinfix += caracter
                    tail.Original(preinfix)
                    infix = ""
                    while tail.isEmpty() == False:
                        infix += tail.desenque() + " "
                    posfix = infix2pos(infix)
                    if posfix == "Preso ":
                        self.pantalla.delete(0, tk.END)
                        self.pantalla.insert(tk.END, "Preso, de la carcel de tus besos, de tu forma de hacer eso a lo que llamas amor") 
                    else:
                        try:
                            valor = round(float(pos2val(posfix)), 4)
                        except ValueError:
                            valor = "Syntax Error"
                        self.pantalla.delete(0, tk.END)
                        self.pantalla.insert(tk.END, valor)
                        self.Infi.config(text="Infix: " + infix)
                        self.Posfi.config(text="Posfix: "+ posfix)
            elif elemento == "destruccion" or elemento == "Pera":
                    pass
            else:
                self.pantalla.insert(tk.END,elemento)

mcr = tk.Tk()
calculadora = Calculadora(mcr)
mcr.mainloop()
#AINH 