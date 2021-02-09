num = 4

#user = True
user = int(input('>>>> '))
while user != num:

    if user < num:
        print('Zbyt mala')
        user = int(input('>>>> '))
