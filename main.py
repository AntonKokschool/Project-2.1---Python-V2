# Main module for PyDuino
import check_serial

listPorts = check_serial.serial_ports()
for i in listPorts:
    print(i, check_serial.readArduino(i))