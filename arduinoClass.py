import serial
import time

class Arduino:

    rollUp = 0.05
    rollDown = 1
    tempeture = 20
    status = ""

    def __init__(self, name, port):
        self.name = name
        self.port = port
        self.ser = serial.Serial(port=port, baudrate=19200, timeout=1)

    def openConnection(self):
        # Close connection
        self.ser.close()
        # Try to open a connection with ser
        try:
            self.ser.open()
            open = True
        except:
            open = False

        time.sleep(0.5)
        return open


    # Write to Arduino
    def writeArduino(self, command, connection):
        # Read output if connection is opened
        if (connection):
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
        triesLeft = 5
        while (triesLeft > 0):
            try:
                ret = self.writeArduino('Status')
                if (ret == ('OK', 'Rolled up')):
                    self.status = 'Rolled up'
                elif (ret == ('OK', 'Rolled down')):
                    self.status = 'Rolled down'
                else:
                    triesLeft -= 1
            except:
                print('Error')
        return self.status