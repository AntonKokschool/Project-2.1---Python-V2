import serial
import time
"""

klasse arduino vanuit  oogpunt van layout

    mockup voorbeeld                                     wat moet het doen      done/moeilijkheden
    poort weergeven                                      return                 gedaan
    naam weergeven                                       return                 gedaan
    oprol                                                static variable        weet niet hoe static werkt
    uitrol de maximale uitrol afstand                    aanpasbare variable    gedaan
    status waar is de arduino mee bezig                  return                 gedaan
    licht kan 3 waarden hebben "bright, light or dim"    return                 gedaan
    temperatuur weergaven                                return                 gedaan
    automatisch                                          ????                   ik weet niet hoe dit eruit moet zien
    handmatig                                            ????                   ik weet niet hoe dit eruit moet zien
    vergrendelen                                         ????                   ik weet niet hoe dit eruit moet zien

"""

listLight = ["bright", "light", "dim"]


class Arduino:

    rollUp = 0.05
    rollDown = 1
    tempeture = 20
    status = "bezig"

    def __init__(self, name, port, listLight):
        self.name = name
        self.port = port
        self.listLight = listLight
        self.ser = serial.Serial(port=port, baudrate=19200, timeout=1)

    # Read output from Arduino
    def readArduino(self):
        # Close all connections
        self.ser.close()
        # Declare stop sign
        stop = (b'\n').decode('ascii')
        # Try to open a connection with ser
        try:
            self.ser.open()
            open = True
        except:
            open = False
        # Declare string for return statement
        word = ''
        # Read output if connection is opened
        if (open):
            # Read from ser
            while (open):
                # Try to read from ser
                try:
                    read = self.ser.read().decode('ascii')
                    # Return word if stop sign was given
                    if (read == stop):
                        return word
                        exit()
                    # Update word with next character
                    else:
                        word += read
                except Exception:
                    # Give error if connection failed
                    error = 'Cannot open serial port'
                    return error

    # Write to Arduino
    def writeArduino(self, command):
        # Read output if connection is opened
        if (open):
            self.ser.write((command + "\n").encode('ascii'))
            extra_info = None
            l = self.ser.readline().decode('ascii').strip()
            if l not in ["OK", "ERR"]:
                extra_info = l
                l = self.ser.readline().decode('ascii').strip()
                if l not in ["OK", "ERR"]:
                    l = None
            return (l, extra_info)

    def returnName(self):
        return self.name

    def returnPort(self):
        return self.port

    def returnRollUp(self):
        return self.rollUp

    def returnRollDown(self):
        return self.rollDown

    def returnLight(self):
        return self.listLight

    def returnTempeture(self):
        return self.tempeture

    def returnStatus(self):
        return self.status


test = Arduino('test', 'COM4', listLight[1])

test.writeArduino('Status')
test.writeArduino('Status')
test.writeArduino('Rol down')
time.sleep(2)
test.writeArduino('Rol up')