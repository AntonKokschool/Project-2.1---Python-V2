import checkSerial
import arduinoClass
listLight = ["bright", "light", "dim"]

def availableArduinos():
    ports = checkSerial.serialPorts()
    arduinos = {}

    for port in ports:
        arduinos[port] = arduinoClass.Arduino('Arduino',port,listLight)

    availableArduinos = []

    for port in ports:
        connection = arduinos[port].openConnection()

        triesLeft = 5
        while (triesLeft > 0):
            try:
                response = arduinos[port].writeArduino('Are you Arduino?', connection)
                triesLeft -= 1
                if (response == ('OK', 'I am Arduino!')):
                    triesLeft = 0
                    availableArduinos.append(port)
            except:
                print("ERROR")

    return availableArduinos