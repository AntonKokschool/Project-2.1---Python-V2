import serial
import time
import sys

# >>> b'a string'.decode('ascii')
# 'a string'
# >>> 'a string'.encode('ascii')
# b'a string'

ser = serial.Serial('COM3', 19200, timeout=1)


# Functie request
#    argment: command -> commando voor Arduino
#    return value: tuple met daarin statuscode (OK of ERR) en evt. aanvullende info
def request(command):
    ser.write((command + "\n").encode('ascii'))  # Let op! pyserial heeft geen writeline, zelf \n aan string toevoegen!
    extra_info = None
    l = ser.readline().decode('ascii').strip()
    if l not in ["OK", "ERR"]:
        extra_info = l
        l = ser.readline().decode('ascii').strip()
        if l not in ["OK", "ERR"]:
            l = None
    return (l, extra_info)


# Handshake
tries_left = 3
while (tries_left > 0):
    r = request("hello")
    if r == ("OK", "IkBenEr!"):
        tries_left = 0
    else:
        tries_left -= 1
        if (tries_left == 0):
            print("Handshake failed")
            sys.exit(1)

# Informatie opvragen
r = request("info")
if (r[0] == "OK"):
    print("Informatie embedded software: " + r[1]);
else:
    print("Fout opgetreden bij opvragen informatie embedded software");

# Met ledjes spelen
request("led1uit")
request("led2uit")
commands = ["led1aan", "led2aan", "led1uit", "led2uit", "ietsraars"]
while (True):
    for command in commands:
        r = request(command)
        print(command + ": " + str(r))
        time.sleep(0.5)
