import time
import socket
import threading
import logging
from logging.handlers import RotatingFileHandler
import sys

def startRttServer():
    logger = logging.getLogger('test.py')
    logger.setLevel(logging.DEBUG)
    # create a file e
    handler = RotatingFileHandler('rtt.log', maxBytes=1*1024*1024, backupCount=1)
    handler.setLevel(logging.DEBUG)

    # # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # add the file handler to the logger
    logger.addHandler(handler)

    port = 9090 # socket server port number
    host = "127.0.0.1"
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    while True:
        try:
            time.sleep(0.2)
            data = client_socket.recv(1024).decode()  # receive response
            if(len(data) > 0):
                try:
                    logger.debug(data)
                except Exception as e:
                    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                    logger.debug(e)
        except Exception as e:
            logger.debug(e)
            client_socket.close()  # close the connection
            client_socket.connect((host, port))  # connect to the server




x = threading.Thread(target = startRttServer)
x.start()
