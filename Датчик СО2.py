import serial
ser = serial.Serial('dev/serial0', baudrate =9600, timeout =1)
ser.write(bytearray([0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]))
response = ser.read(9)
if len(response) == 9:
    co2 = response[2] * 256 + response[3]
    print(f"CO2: {co2} ppm")
    
