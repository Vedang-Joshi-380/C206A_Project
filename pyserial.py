import serial

s = serial.Serial('/dev/tty.usbmodem1101', 115200)  # Adjust port and baud rate accordingly
print(s.name)

string = s.name.encode()
s.write(string)  # Send data to Pico
data = s.readline()  # Read data from Pico
print(data.decode())  # Decode the received data
