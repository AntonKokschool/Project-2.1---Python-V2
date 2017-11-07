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
Version: 2017-11-07
"""

# List al Arduino's
def checkArduino():
    listArduino = []

    ser_ports = serial_ports()
    bautrate = 19200 # Bautrate for connection
    timeoutValue = 1 # Timeout value for conection

    # Tests connection for every found port
    for port in ser_ports:

        ser = serial.Serial(port, bautrate, timeout=timeoutValue)

        handshake = ser.readline().decode('ascii').strip()
        if handshake == 'Arduino\n':
            listArduino.append(port)

    # Display all found Arduino's
    if len(listArduino) == 0:
        print("No Arduino('s) were found.")
    else:
        print("Arduino('s) found on port:")

        for arduino in listArduino:
            print(arduino)

#    ser.write((command + "\n").encode('ascii'))
#    l = ser.readline().decode('ascii').strip()