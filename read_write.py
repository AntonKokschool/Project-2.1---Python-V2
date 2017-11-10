import serial

def getPort():
    return 'COM4'



ser = serial.Serial(port=getPort(), baudrate=19200, timeout=1)

# Read output from Arduino
def readArduino():
    # Close all connections
    ser.close()
    # Declare stop sign
    stop = (b'\n').decode('ascii')
    # Try to open a connection with ser
    try:
        ser.open()
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
                read = ser.read().decode('ascii')
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
def writeArduino(command):
    # Declare string for return statement
    word = ''
    # Read output if connection is opened
    if (open):
        ser.write((command + "\n").encode('ascii'))
        extra_info = None
        l = ser.readline().decode('ascii').strip()
        if l not in ["OK", "ERR"]:
            extra_info = l
            l = ser.readline().decode('ascii').strip()
            if l not in ["OK", "ERR"]:
                l = None
        return (l, extra_info)