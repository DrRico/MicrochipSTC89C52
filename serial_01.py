import time
import serial

ser = serial.Serial(
    port='COM4',
    baudrate=9600,
    parity=serial.PARITY_ODD,  # 校验位
    stopbits=serial.STOPBITS_TWO,  # 停止位
    bytesize=serial.SEVENBITS  # 数据位
)
data = ''

while True:
    data = ser.readline()
    if data ==b'\r\n':
        continue
    t = time.time()
    ct = time.ctime(t)
    print(ct, ':')
    print(data)

    #f = open('data_1.txt', 'a')
    f = open('July07_empty_temp_4.txt', 'a')
    f.writelines(data.decode('utf-8'))
    f.close()