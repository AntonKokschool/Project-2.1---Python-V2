import checkSerial
import arduinoClass
import portClass
import os
from tkinter import *

# Create portClass instance
currentPort = portClass.port()

# Check all ports
ports = checkSerial.serialPorts()
# Create dict for making a object for every port
arduinos = {}

# Make an object from Arduino class for every found port
for port in ports:
    arduinos[port] = arduinoClass.Arduino('Arduino', port)

# List for every acutal Arduino
availableArduinos = []

# Test if port is an Arduino
for port in ports:
    connection = arduinos[port].openConnection()

    # Tries max 5 times
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

# Start PyDuino
def run():
    pyduino.mainloop()

# Function for home button
def home():
    print("ga naar home")

# Function for Arduino button
def arduinoPage(port):
    currentPort.setPort(port)

# Function for close button
def close():
    pyduino.destroy()

# Function fot restarting
def printPort():
    print(currentPort.getPort())

# Function for receiving status from Arduino
def getStatus():
    port = currentPort.getPort()
    status = arduinos[port].writeArduino('Status', True)
    print(status)

# Function for rolling up
def rollUp():
    port = currentPort.getPort()
    status = arduinos[port].writeArduino('Rol up', True)
    print(status)
    getStatus()

# Function for rolling up
def rollDown():
    port = currentPort.getPort()
    status = arduinos[port].writeArduino('Rol down', True)
    print(status)
    getStatus()

# Define PyDuino GUI
pyduino = Tk()

# Define row
row = 1
# Define button width
buttonWidth = "15"

# Set icon
pyduino.iconbitmap('PyDuino.ico')
# Set window name
pyduino.title('PyDuino')
# Set frame size for pyduino
pyduino.geometry("600x500")
# Set status bar
status = Label(pyduino, text="© European IT Company - Zeng Ltd.", bd=1, relief=SUNKEN, anchor=W)
# Define row for statusbar
status.pack(side=BOTTOM, fill=X)
# Set background color for content bar
menuFrame = Frame(pyduino, bg="#3776AA")
# Define home button
home = Button(menuFrame, text="Hoofdscherm", command=home)
home.grid(row=0, padx=2, pady=2)
home.config(width=buttonWidth)
menuFrame.pack(side=LEFT, fill=Y)

# Create button for for every available Arduino
for arduino in availableArduinos:
    arduino = Button(menuFrame, text=arduino, command=arduinoPage(arduino))
    arduino.grid(row=row, padx=2, pady=2)
    arduino.config(width=buttonWidth)
    row += 1 # Update row

# Define close button
restart = Button(menuFrame, text='Print huidige port', command=printPort)
restart.grid(row=row, padx=2, pady=2)
restart.config(width=buttonWidth)
row += 1 # Update row
close = Button(menuFrame, text='Afsluiten', command=close)
close.grid(row=row, padx=2, pady=2)
close.config(width=buttonWidth)

# Set background color for canvas
canvasFrame = Frame(pyduino)
canvasFrame.pack(side=RIGHT, fill=Y)
# Define row for button row
row = 1
# Define button width
buttonWidth = "15"

# Define row
row = 0
# Define button width
buttonWidth = "15"

# Create image
image = PhotoImage(file='PyDuino.png')
imageLabel = Label(canvasFrame, image=image, justify=RIGHT, width=400)
imageLabel.grid(row=row, padx=2, pady=2)
row += 1 # Update row

# Create status button and label
statusButton = Button(canvasFrame, text='Vraag status op', command=getStatus)
statusButton.config(width=buttonWidth)
statusButton.grid(row=row, padx=2, pady=2)
row += 1 # Update row

# Create roll up button
rollUpButton = Button(canvasFrame, text='Rol scherm op', command=rollUp)
rollUpButton.config(width=buttonWidth)
rollUpButton.grid(row=row, padx=2, pady=2)
row += 1 # Update row

# Create roll down button
rollDownButton = Button(canvasFrame, text='Rol scherm uit', command=rollDown)
rollDownButton.config(width=buttonWidth)
rollDownButton.grid(row=row, padx=2, pady=2)
row += 1 # Update row

# Run PyDuino
run()
