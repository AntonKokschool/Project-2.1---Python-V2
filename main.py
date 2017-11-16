import checkSerial
import arduinoClass
import os
from tkinter import *

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
def arduinoPage():
    print("ArduinoPage")

# Function for close button
def close():
    pyduino.destroy()

# Function fot restarting
def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Define PyDuino GUI
pyduino = Tk()

# Set icon
pyduino.iconbitmap('PyDuino.ico')
# Set window name
pyduino.title('PyDuino')
# Set frame size for pyduino
pyduino.geometry("600x500")
# Set status bar
status = Label(pyduino, text="© European IT Company - Zeng Ltd.", bd=1, relief=SUNKEN, anchor=W)
# Define position for statusbar
status.pack(side=BOTTOM, fill=X)
# Set background color for content bar
backgroundFrame = Frame(pyduino, bg="#3776AA")
# Define home button
home = Button(backgroundFrame, text="Hoofdscherm", command=home)

# Define row for button position
row = 1
# Define button width
buttonWidth = "15"

# Define home button
home.grid(row=0, padx=2, pady=2)
home.config(width=buttonWidth)
backgroundFrame.pack(side=LEFT, fill=Y)

# Create button for for every available Arduino
for arduino in availableArduinos:
    arduino = Button(backgroundFrame, text=arduino, command=arduinoPage)
    arduino.grid(row=row, padx=2, pady=2)
    arduino.config(width=buttonWidth)
    row += 1 # Update row

# Define close button
restart = Button(backgroundFrame, text='Herstarten', command=restart)
restart.grid(row=row, padx=2, pady=2)
restart.config(width=buttonWidth)
row += 1 # Update row

# Define close button
close = Button(backgroundFrame, text='Afsluiten', command=close)
close.grid(row=row, padx=2, pady=2)
close.config(width=buttonWidth)

# Create image
image = PhotoImage(file='PyDuino.png')
imageLable = Label(pyduino, image=image, justify=RIGHT, width=400)
imageLable.pack()

# Run PyDuino
run()
