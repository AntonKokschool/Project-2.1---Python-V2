'''

hierin staat de layout van settings
let op er moeten nog voorwaarden voor de error berichten worden geschreven
knop toepassen en uit breiden

'''

from tkinter import *

setting = Tk()

poortVar = "COM4"

"""
labels namen geven
"""

naam = Label(setting, text="Naam:")
uitrol = Label(setting, text="Uitrol:")
licht = Label(setting, text="licht:")
poort = Label(setting, text="Poort:")
poortNaam = Label(setting, text=poortVar)

def aply():
    print('Toegepast')
    setting.destroy()

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
invoerNaam = Entry(setting)
invoerUitrol = Entry(setting)
invoerLicht = Entry(setting)

"""
locatie invoervelden
"""

invoerNaam.grid(row=0, column=1)
invoerUitrol.grid(row=1, column=1)
invoerLicht.grid(row=2, column=1)

"""
knoppen maken
"""
aply = Button(setting, text="Toepassen", command=aply)

"""
locatie knoppen
"""
aply.grid(row=4, sticky=W)

"""
error label maken
"""
naamError = Label(setting, text="invoerveld 'Naam' is niet  goed ingevuld", fg="red")
uitrolError = Label(setting, text="invoerveld 'Uitrol' is niet goed ingevuld", fg="red")
lichtError = Label(setting, text="invoerveld 'licht' is niet goed ingevuld", fg="red")

"""
error locatie
"""

naamError.grid(row=0, column=2, sticky=W)
uitrolError.grid(row=1, column=2, sticky=W)
lichtError.grid(row=2, column=2, sticky=W)

setting.mainloop()