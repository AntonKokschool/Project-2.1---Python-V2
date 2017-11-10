"""

hier staat de lijst en home knop van arduino (zijkant van mockups)

"""

from tkinter import *

"""
functies van knoppen
"""

def home():
    print("ga naar home")

def arduino_1():
    print("ga naar arduino 1")

def arduino_2():
    print("ga naar arduino 2")

def arduino_3():
    print("ga naar arduino 3")

def arduino_4():
    print("ga naar arduino 4")

def arduino_5():
    print("ga naar arduino 5")

root = Tk()

"""
geeft aan de onderkant van het beeld de status van de handshake weer.
vervang text variable status handshake met de variable
"""
status = Label(root, text="variable status handshake", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

"""
arduino lijst/overzicht aan de zijkant
"""

"""
maak de achtergrond blauw
"""
arduinoOverzicht = Frame(root, bg="blue")

"""
initaliseren van knoppen
naam van de knop kan aangepast worden door het woord na text
"""

home = Button(arduinoOverzicht, text="overzicht", command=home)

arduino_1 = Button(arduinoOverzicht, text="arduino 1", command=arduino_1)

arduino_2 = Button(arduinoOverzicht, text="arduino 2", command=arduino_2)

arduino_3 = Button(arduinoOverzicht, text="arduino 3", command=arduino_3)

arduino_4 = Button(arduinoOverzicht, text="arduino 4", command=arduino_4)

arduino_5 = Button(arduinoOverzicht, text="arduino 5", command=arduino_5)


"""
geeft de locatie weer van de knoppen
row geeft de volg orde van boven naar beneden
padx geeft het aantal pixels die links en rechts van de knop leeg blijft
pady geeft het aantal pixels dat boven en onder van de knop leeg blijft
"""
home.grid(row=0, padx=2, pady=2)

arduino_1.grid(row=1, padx=2, pady=2)

arduino_2.grid(row=2, padx=2, pady=2)

arduino_3.grid(row=3, padx=2, pady=2)

arduino_4.grid(row=4, padx=2, pady=2)

arduino_5.grid(row=5, padx=2, pady=2)

"""
zet alles aan de linker kant en vult het frame van boven naar beneden (het frame is blauw dus maakt het blauw langs de zijkant)
"""
arduinoOverzicht.pack(side=LEFT, fill=Y)

root.mainloop()
