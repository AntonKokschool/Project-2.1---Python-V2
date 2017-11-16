import checkSerial
import arduinoClass
from tkinter import *

listLight = ["bright", "light", "dim"]

ports = checkSerial.serialPorts()
arduinos = {}

for port in ports:
    arduinos[port] = arduinoClass.Arduino('Arduino',port,listLight)

availableArduinos = []

for port in ports:
    connection = arduinos[port].openConnection()

    triesLeft = 5
    while (triesLeft > 0):
        try:
            response = arduinos[port].writeArduino('Are you Arduino?', connection)
            triesLeft -= 1
            if (response == ('OK', 'I am Arduino!')):
                triesLeft = 0
                availableArduinos.append(port)
        except:
            print("ERROR")

def home():
    print("ga naar home")

def arduinoPage(port):
    print('Hello')

def close():
    pyduino.destroy()

# Define PyDuino GUI
pyduino = Tk()
# Set icon
pyduino.iconbitmap('PyDuino.ico')
# Set window name
pyduino.title('PyDuino V2')
# Set frame size for pyduino
pyduino.geometry("500x500")
# Set status bar
status = Label(pyduino, text="© European IT Company - Zeng Ltd.", bd=1, relief=SUNKEN, anchor=W)
# Define position for statusbar
status.pack(side=BOTTOM, fill=X)
# Set background color for content bar
backgroundFrame = Frame(pyduino, bg="blue")

home = Button(backgroundFrame, text="Hoofdscherm", command=home)
empty = []

len = len(availableArduinos)
row = 1

if (len > 0):
    for arduino in availableArduinos:
        arduino = Button(backgroundFrame, text=arduino, command=arduinoPage)
        arduino.grid(row=row, padx=2, pady=2)
        row += 1

close = Button(backgroundFrame, text='Afsluiten', command=close)
close.grid(row=row, padx=2, pady=2)

home.grid(row=0, padx=2, pady=2)
backgroundFrame.pack(side=LEFT, fill=Y)

pyduino.mainloop()
