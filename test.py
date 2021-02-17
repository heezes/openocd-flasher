import time
import socket
import threading
try:
    from gpiozero import LED, Button
except Exception as e:
    print(e.args)


def startRttServer():
    port = 9090 # socket server port number
    host = "127.0.0.1"
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    while True:
        time.sleep(0.2)
        data = client_socket.recv(1024).decode()  # receive response
        if(len(data) > 0):
            print(data)

    client_socket.close()  # close the connection



x = threading.Thread(target = startRttServer)
x.start()
try:
    key_pin = LED(6)
except Exception as e:
   print(e)
while(True):
    time.sleep(1)
    case = int(input("Run Test Case: "))
    if case == 1:
        key_pin.on()
        print("Unlocking")
    elif case == 2:
        key_pin.off()
        print("Locking")
    else:
        pass
    case = 0
