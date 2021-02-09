with open('kaczka.txt') as f:
    read = f.read()

with open('kaczka2.txt', 'w') as f:
    write = f.write(read)