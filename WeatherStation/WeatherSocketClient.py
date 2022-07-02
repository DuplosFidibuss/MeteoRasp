import socket
import logfile

HOST = '192.168.1.107'
PORT = 12345

def send_data(data: str, is_log: bool):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        if is_log:
            s.send(bytes('log'+data, 'utf-8'))
        else:
            s.send(bytes(data, 'utf-8'))
    except:
        logfile.write(data)
    s = 0

def send_log():
    log = logfile.read()
    if not log == '':
        logfile.clear()
        for line in log.split('\n'):
            if not line == '':
                send_data(line, True)
