import serial
i = 'COM1'

# Define serial connection
ser = serial.Serial(port=i, baudrate=19200, timeout=1)
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
    try:
        # Read from ser
        while(open):
            read = ser.read().decode('ascii')
            # Return word if stop sign was given
            if (read == stop):
                print(word)
                exit()
            # Update word with next character
            else:
                word += read
    except Exception:
        # Give error if connection failed
        error = 'Cannot open serial port'
        print(error)