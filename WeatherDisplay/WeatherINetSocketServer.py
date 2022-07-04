import socket
import sys
import logfile
from WeatherDisplay import *

HOST = '10.128.0.15'
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error:
    print('bind failed')

surf, font = init_display()

try:
    while True:
        s.listen(1)
        (conn, address) = s.accept()
        data = str(conn.recv(1024)).strip("b'")
        conn.close()
        if not data.startswith('log'):
            weather_data = WeatherData(data)
            update_display(surf, font, weather_data)
        else:
            data = data.strip('log')
        logfile.write(data)
except KeyboardInterrupt:
    pass
finally:
    close_display()
    sys.exit()
