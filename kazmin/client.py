import socket

IP = '127.0.0.1'
PORT = 1005
buffersize = 65535

s = socket.socket()
s.connect((IP, PORT))
print("Соединение с сервером " + IP + ":" + str(PORT) + " установлено.\n")

while True:
    print("Команды:")
    print("1 Log file посмотреть")
    if pckType == 1:
        data = input("Введите путь: ")
        pckSend = chr(pckType) + data
        s.send(bytearray(pckSend, 'utf-8'))
        pckRecv = s.recv(buffersize).decode("utf-8")
s.close()
print("Соединение закрыто.")