def write(data: str):
    with open ('log.txt', 'a') as log:
        log.write(data+'\n')

def read():
    data = ''
    with open ('log.txt') as log:
        data = log.read()
    return data

def clear():
    with open ('log.txt', 'w') as log:
        log.write('')
