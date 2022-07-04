import socket
import sys
import logfile

HOST = 'B8:27:EB:BA:29:E7'
PORT = 3

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error:
    print('bind failed')

try:
    while True:
        s.listen(1)
        (conn, address) = s.accept()
        data = str(conn.recv(1024)).strip("b'")
        log = logfile.read()
        if not log == '':
            s.send(bytes(log, 'utf-8'))
        conn.close()
        logfile.clear()
except KeyboardInterrupt:
    pass
finally:
    sys.exit()
