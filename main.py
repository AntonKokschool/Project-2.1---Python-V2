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

def update():
    port = currentPort.getPort()
    if port == '':
        text = 'Selecteer een zonnescherm uit het linker menu'
    else:
        text = 'Huidig zonnescherm: ' + port
        arduinoLabel.config(text=text)
        printStatus()

# Function for home button
def home():
    print("ga naar home")

# Function for Arduino button
def arduinoPage(port):
    currentPort.setPort(port)

# Function for close button
def closeGUI():
    pyduino.destroy()

# Function for receiving status from Arduino
def getStatus():
    port = currentPort.getPort()
    status = arduinos[port].writeArduino('Status', True)
    return status

# Function for
def printStatus():
    portStat = currentPort.getPort()
    if portStat == (''):
        statusLabel.config(text='Status niet beschikbaar')
        pass
    status = getStatus()
    if status[0] == ('OK'):
        if status[1] == ('Rolled down'):
            statusLabel.config(text='Status: Uitgerold')
        if status[1] == ('Rolled up'):
            statusLabel.config(text='Status: Opgerold')

# Function for rolling up
def rollUp():
    port = currentPort.getPort()
    arduinos[port].writeArduino('Rol up', True)
    for i in range(5):
        update()

# Function for rolling up
def rollDown():
    port = currentPort.getPort()
    arduinos[port].writeArduino('Rol down', True)
    for i in range(5):
        update()

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

# Define update button
portButton = Button(menuFrame, text='Update', command=update)
portButton.grid(row=row, padx=2, pady=2)
portButton.config(width=buttonWidth)
row += 1 # Update row

# Define close button
close = Button(menuFrame, text='Afsluiten', command=closeGUI)
close.grid(row=row, padx=2, pady=2)
close.config(width=buttonWidth)

# Setup canvas
canvasFrame = Frame(pyduino)
canvasFrame.pack(fill=Y)

# Setup image
image = PhotoImage(file='PyDuino.png')
# Setup image
imageLabel = Label(canvasFrame, image=image, justify=RIGHT, width=400)
# Setup status label
arduinoLabel = Label(canvasFrame)
# Setup status label
statusLabel = Label(canvasFrame)
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

# Create Arduino label
arduinoLabel.config(text='Selecteer een zonnescherm uit het linker menu')
arduinoLabel.grid(row=row, padx=2, pady=2)
row += 1 # Update row

# Create status label
statusLabel.config(text='Status niet beschikbaar')
statusLabel.grid(row=row, padx=2, pady=2)
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
