with open('kaczka2.txt') as f:
    read = f.readlines()

print(read)
list1 = []
for element in read:
    if element == '\n':
        pass
    else:
        element = element.rstrip('\n')
        if element != 'pies':
            print(element)

            list1.append(element)

print(list1)
for element in list1:
    with open('kaczka3.txt', 'a') as f:
        f.write(f'{element}\n')