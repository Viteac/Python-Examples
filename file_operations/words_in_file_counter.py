with open('words.txt','r') as f:
    read = f.readlines()

print(read)
slowa = []
for line in read:
    line = line.rstrip('\n')
    print(line)
