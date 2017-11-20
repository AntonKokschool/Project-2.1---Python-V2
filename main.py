import checkSerial
import arduinoClass
import portClass
from tkinter import *

# Create portClass instance
currentPort = portClass.port()

# Check all ports
ports = checkSerial.serialPorts()
# Create dict for making an object for every port
arduinos = {}
# Create dict for making a button for every Arduino
arduinoButton = {}

# Make an object from Arduino class for every found port
for port in ports:
    arduinos[port] = arduinoClass.Arduino(port)

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
    print('test')

# Function for close button
def close():
    pyduino.destroy()

# Function for receiving status from Arduino
def getStatus():
    port = currentPort.getPort()
    status = arduinos[port].writeArduino('Status', True)
    return status

def printStatus():
    print(getStatus())

# Function for rolling up
def rollUp():
    port = currentPort.getPort()
    status = arduinos[port].writeArduino('Rol up', True)
    print(status)
    triesLeft = 5
    if status == ('OK', 'Already up'):
        triesLeft = 0
    while (triesLeft > 0):
        status = arduinos[port].readArduino(True)
        print(status)
        triesLeft -= 1

# Function for rolling up
def rollDown():
    port = currentPort.getPort()
    status = arduinos[port].writeArduino('Rol down', True)
    print(status)
    status = arduinos[port].readArduino(True)
    print(status)

def getPort():
    port = currentPort.getPort()
    print(port)

# Define PyDuino GUI
pyduino = Tk()

# Set icon
pyduino.iconbitmap('PyDuino.ico')
# Set window name
pyduino.title('PyDuino')
# Set frame size for pyduino
pyduino.geometry("550x500")
# Set status bar
status = Label(pyduino, text="© European IT Company - Zeng Ltd.", bd=1, relief=SUNKEN, anchor=W)
# Define row for statusbar
status.pack(side=BOTTOM, fill=X)
# Set background color for content bar
menuFrame = Frame(pyduino, bg="#3776AA")
menuFrame.pack(side=LEFT, fill=Y)

# Setup close button
close = Button(menuFrame, text='Afsluiten', command=close)

# Define row
row = 0
# Define button width
buttonWidth = "15"

# Create button for for every available Arduino
for arduino in availableArduinos:
    name = arduino
    arduinoButton[arduino] = Button(menuFrame, text=name, command=lambda arduino=arduino: arduinoPage(arduino))
    arduinoButton[arduino].grid(row=row, padx=2, pady=2)
    arduinoButton[arduino].config(width=buttonWidth)
    row += 1 # Update row

# Define get port button
portButton = Button(menuFrame, text='Print port', command=getPort)
portButton.grid(row=row, padx=2, pady=2)
portButton.config(width=buttonWidth)
row += 1 # Update row

# Define close button
close.grid(row=row, padx=2, pady=2)
close.config(width=buttonWidth)

# Set background color for canvas
canvasFrame = Frame(pyduino)
canvasFrame.pack(fill=Y)

# Setup image
image = PhotoImage(file='PyDuino.png')
# Setup status button and label
statusButton = Button(canvasFrame, text='Vraag status op', command=printStatus)
# Setup image
imageLabel = Label(canvasFrame, image=image, justify=RIGHT, width=400)
# Setup roll up button
rollUpButton = Button(canvasFrame, text='Rol scherm op', command=rollUp)
# Setup roll down button
rollDownButton = Button(canvasFrame, text='Rol scherm uit', command=rollDown)

# Define row for button row
row = 1
# Define button width
buttonWidth = "15"

# Create image
imageLabel.grid(row=row, padx=2, pady=2)
row += 1 # Update row

# Create status button and label
statusButton.config(width=buttonWidth)
statusButton.grid(row=row, padx=2, pady=2)
row += 1 # Update row

# Create roll up button
rollUpButton.config(width=buttonWidth)
rollUpButton.grid(row=row, padx=2, pady=2)
row += 1 # Update row

# Create roll down button
rollDownButton.config(width=buttonWidth)
rollDownButton.grid(row=row, padx=2, pady=2)
row += 1 # Update row

# Run PyDuino
run()
