def send_data(data: str):
    import socket
    
    HOST = 'B8:27:EB:BA:29:E7'
    PORT = 3
    
    try:
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.connect((HOST, PORT))
        s.send(data)
        s.close()
    except:
        with open('log.txt', 'a') as log:
            log.write(data)
            log.write('\n')
