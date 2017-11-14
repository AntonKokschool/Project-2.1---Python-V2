"""

hierin heb ik een poging gedaan om een klasse voor knoppen te maken (het is overigens niet echt gelukt)

"""

from tkinter import *


class Knoppen:

    def bericht(self):
        print("werkt dit?")

    def tweede(self):
        print("test")

    def __init__(self, master):
        beeld = Frame(master)
        beeld.pack()

        self.printButton = Button(beeld, text="Print Message", command=self.bericht)
        self.printButton.pack(side=LEFT)

        self.tweedeButton = Button(beeld, text="Print Message", command=self.tweede)
        self.tweedeButton.pack(side=LEFT)


window = Tk()

app = Knoppen(window)


def leftClick(klik):
    print("left")


def middleClick(klik):
    print("middle")


def rightClick(klik):
    print("right")


frame = Frame(window, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

window.mainloop()