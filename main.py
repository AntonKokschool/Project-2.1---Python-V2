# Main module for PyDuino
import read_write

triesLeft = 5
i = 0
foundArduino = False

while (triesLeft > 0):
    r = read_write.writeArduino('Are you Arduino?')
    print(r)
    triesLeft -= 1

