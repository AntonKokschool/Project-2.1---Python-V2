'''

hierin staat de layout van settings
let op er moeten nog voorwaarden voor de error berichten worden geschreven
knop toepassen en uit breiden

'''

from tkinter import *

root = Tk()

poortVar = "COM4"

"""
labels namen geven
"""

naam = Label(root, text="Naam:")
uitrol = Label(root, text="Uitrol:")
licht = Label(root, text="licht:")
poort = Label(root, text="Poort:")
poortNaam = Label(root, text=poortVar)

"""
locatie van de labels
"""
naam.grid(row=0, sticky=W)
uitrol.grid(row=1, sticky=W)
licht.grid(row=2, sticky=W)
poort.grid(row=3, sticky=W)
poortNaam.grid(row=3, column=1)

"""
invoervelden maken
"""
invoerNaam = Entry(root)
invoerUitrol = Entry(root)
invoerLicht = Entry(root)

"""
locatie invoervelden
"""

invoerNaam.grid(row=0, column=1)
invoerUitrol.grid(row=1, column=1)
invoerLicht.grid(row=2, column=1)

"""
knoppen maken
"""
toepassen = Button(root, text="toepassen")

"""
locatie knoppen
"""
toepassen.grid(row=4, sticky=W)

"""
error label maken
"""
naamError = Label(root, text="invoerveld 'Naam' is niet  goed ingevuld", fg="red")
uitrolError = Label(root, text="invoerveld 'Uitrol' is niet goed ingevuld", fg="red")
lichtError = Label(root, text="invoerveld 'licht' is niet goed ingevuld", fg="red")

"""
error locatie
"""

naamError.grid(row=0, column=2, sticky=W)
uitrolError.grid(row=1, column=2, sticky=W)
lichtError.grid(row=2, column=2, sticky=W)

root.mainloop()