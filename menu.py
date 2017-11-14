import availableArduinos
"""

hier staat de lijst en home knop van arduino (zijkant van mockups)

"""

from tkinter import *

"""
functies van knoppen
"""

def home():
    print("ga naar home")

def arduinoPage():
    print('Hello!')

def close():
    root.destroy()

root = Tk()


"""
geeft aan de onderkant van het beeld de status van de handshake weer.
vervang text variable status handshake met de variable
"""
status = Label(root, text="© European IT Company", bd=1, relief=SUNKEN, anchor=W)
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

home = Button(arduinoOverzicht, text="Hoofdscherm", command=home)

availableArduinos = availableArduinos.availableArduinos()
empty = []

len = len(availableArduinos)
row = 1

if (len > 0):
    for arduino in availableArduinos:
        arduino = Button(arduinoOverzicht, text=arduino, command=arduinoPage)
        arduino.grid(row=row, padx=2, pady=2)
        row += 1

close = Button(arduinoOverzicht, text='Afsluiten', command=close)
close.grid(row=row, padx=2, pady=2)
"""
geeft de locatie weer van de knoppen
row geeft de volg orde van boven naar beneden
padx geeft het aantal pixels die links en rechts van de knop leeg blijft
pady geeft het aantal pixels dat boven en onder van de knop leeg blijft
"""

home.grid(row=0, padx=2, pady=2)
"""
zet alles aan de linker kant en vult het frame van boven naar beneden (het frame is blauw dus maakt het blauw langs de zijkant)
"""
arduinoOverzicht.pack(side=LEFT, fill=Y)

def setupMenu():
    root.mainloop()
