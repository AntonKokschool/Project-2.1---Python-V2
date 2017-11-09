# Main module for PyDuino
import read_write
import time

triesLeft = 5
i = 0
foundArduino = False

def ledBlink():
    i = 3
    commands = ['led1aan','led2aan','led1uit','led2uit']
    while i > 0:
        for command in commands:
            read_write.writeArduino(command)
            print(command, i)
            time.sleep(0.5)
        i -= 1

try:
    while (i < triesLeft):
        ret = read_write.writeArduino('hello')
        if (ret == ('OK', 'IkBenEr!')):
            ledBlink()
            i = triesLeft
            foundArduino = True
        else:
            triesLeft -= 1
    if (foundArduino):
        print('Arduino was found')
    else:
        print('Arduino was not found')
except:
    print('Arduino was not found')
