# Импорт библиотек
import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#Устанавливаем связь с последовательным портом
con = serial.Serial(

    port='/dev/ttyS0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,

)

#обьявляем переменные с данными передаваемым при нажатии кнопкии на экране
i=[b'e\x00\x01\x01\xff\xff\xff']
y=[b'e\x00\x02\x01\xff\xff\xff']


#Запускаем цикл, который ожидает сигнала с дисплея
while True:
    readTxt = con.readline(7)#Если данные от экрана поступили считываемм 7 байтов данных 
    newByte=[readTxt]#Переводим данные в массив

    if newByte == i:                #Производим сверку полученных данных с эталонными, если данные равны, то              
        GPIO.setup(37, GPIO.OUT)    #Устанавливаем 37 Пин распберри на выход
        GPIO.output(37,0)           #Присваиваем 37 пин значение LOW тем самы открываем реле ВКЛ

    if newByte == y:                #Проверяем данные полученные от второй кнопки, ели равны то
        print("Привет")
        GPIO.setup(37, GPIO.OUT)
        GPIO.output(37,1)           #Закрываем реле ВЫКЛ