import serial
port = 'COM4'

class Arduino():

    def __init__(self, port):
        self.port = port
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
        # Declare string for return statement
        word = ''
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

arduino4 = Arduino('COM4')

triedLeft = 5
while (triedLeft > 0):
    try:
        r = arduino4.writeArduino('Status')
        if (r == ('OK','Rolled up')):
            print(r)
            triedLeft = 0
    except:
     print('Fail')