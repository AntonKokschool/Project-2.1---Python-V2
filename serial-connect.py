import serial

ser = serial.Serial('COM4', 19200, timeout=1)
count = 0

while (True):
    try:
        command = 'Arduino'
        ser.write((command + "\n").encode('ascii'))
        read = ser.readline().decode('ascii').strip()
        print(read)
    except ValueError:
        print('Try failed', count, 'times.')
        count += 1