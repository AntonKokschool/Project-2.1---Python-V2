from tkinter import *

root = Tk()

poortVar = "COM4"

naam = Label(root, text="Naam:")
uitrol = Label(root, text="Uitrol:")
licht = Label(root, text="licht:")
poort = Label(root, text="Poort:")
poortNaam = Label(root, text=poortVar)

naam.grid(row=0, sticky=W)
uitrol.grid(row=1, sticky=W)
licht.grid(row=2, sticky=W)
poort.grid(row=3, sticky=W)
poortNaam.grid(row=3, column=1)

invoerNaam = Entry(root)
invoerUitrol = Entry(root)
invoerLicht = Entry(root)

invoerNaam.grid(row=0, column=1)
invoerUitrol.grid(row=1, column=1)
invoerLicht.grid(row=2, column=1)

toepassen = Button(root, text="toepassen")
toepassen.grid(row=4, sticky=W)

naamError = Label(root, text="invoerveld 'Naam' is niet  goed ingevuld", fg="red")
uitrolError = Label(root, text="invoerveld 'Uitrol' is niet goed ingevuld", fg="red")
lichtError = Label(root, text="invoerveld 'licht' is niet goed ingevuld", fg="red")

naamError.grid(row=0, column=2, sticky=W)
uitrolError.grid(row=1, column=2, sticky=W)
lichtError.grid(row=2, column=2, sticky=W)

root.mainloop()