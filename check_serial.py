import sys
import glob
import serial

# check serial ports module for PyDuino

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system

        Original code disigned by Thomas Feldmann
        GitHub: https://github.com/tfeldmann
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

"""
HANDSHAKE

author:  Ricardo van der Vlag
GitHub:  https://github.com/ricardovandervlag
Version: 2017-11-08
"""
open = False
# Read output from Arduino
def readArduino(i):
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