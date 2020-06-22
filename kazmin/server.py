import time
import socket
import threading
from  test_for_log import openning

IP = ''
PORT = 1005
backlog = 50
buffersize = 65535

s = socket.socket()
s.bind((IP, PORT))
s.listen(backlog)
print("ѕорт " + str(PORT) + " прослушиваетс€...")


def new_connect(sock, addr):
    def send(pckData):
        sock.send(bytearray(pckData, 'utf-8'))

    last_message = chr(0)
    try:
        while True:
            data = sock.recv(buffersize).decode("utf-8")  # получаем данные
            if data == '': break

            pckType = ord(data[0])  # первый байт - тип сетевого пакета

            if pckType == 1:  # 01 - высветить ему лог файл
                a = data[1:]
                openning(a)
                print(addr[0] + " Log file высветить")
sock.close()
        print("—оединение " + addr[0] + " закрыто")
while True:
    sock, addr = s.accept()
    print("Ќовое соединение от " + addr[0])

    threading.Thread(target=new_connect, args=(sock, addr,)).start()  # создаем новый поток