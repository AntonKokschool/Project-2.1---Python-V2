"""

overzicht arduino venster
grafiek mist nog

"""

from tkinter import *

root = Tk()
"""
labels
maakt een label overzicht en maakt het blauw voor de duidelijkheid
"""
overzicht = Label(root, text="Overzicht van arduino's", fg="blue", font="times 24 bold underline")
"""
locatie van labels
"""
overzicht.grid(row=0, column= 2)

"""
functies van knoppen
"""
def uitrollen():
    print("zonnescherm uitrollen")

def oprollen():
    print("zonnescherm oprollen")

def status():
    print("geef status van alle of individuele arduino?")

def toepassen():
    print("instellingen toepassen")

def automatisch():
    print("zet alles op automatisch")

def handmatig():
    print("handmatige bediening")

def vergrendelen():
    print("bedieningen vergrendeld")


"""
initaliseren van knoppen
bij text kun je de naam aanpassen van knoppen
"""
uitrolKnop = Button(root, text="uitrollen", command=uitrollen)

oprolKnop = Button(root, text="oprollen", command=oprollen)

statusKnop = Button(root, text="status", command=status)

toepassenKnop = Button(root, text="toepassen", command=toepassen)

automatischKnop = Button(root, text="automatisch", command=automatisch)

handmatigKnop = Button(root, text="handmatig", command=handmatig)

vergrendelenKnop = Button(root, text="vergrendelen", command=vergrendelen)

"""
geeft de locatie van knoppen
row werk ik met tientallen omdat ik dan makkelijker van plek kan laten wisselen
sticky zorgt dat de knop goed uitlijnt
"""
uitrolKnop.grid(row=10, column=2, sticky=W)

oprolKnop.grid(row=20, column=2, sticky=W)

statusKnop.grid(row=21, column=2, sticky=W)

toepassenKnop.grid(row=30, column=2, sticky=W)

automatischKnop.grid(row=40, column=2, sticky=W)

handmatigKnop.grid(row=50, column=2, sticky=W)

vergrendelenKnop.grid(row=60, column=2, sticky=W)

root.mainloop()