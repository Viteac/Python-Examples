import os
print('---------------------------------')
print('<<<<<<< Bulk File Rename >>>>>>>')
print('---------------------------------')
print('')


def check_path():
    while True:
        print('Enter a full path to folder you want to change files in')
        folders = input('Enter a path: ')
        if os.path.isdir(folders) is True:
            if folders.endswith('/') is True:
                print('You want to change')
                return folders
            else:
                folders = f'{folders}/'
                return folders


def enumeration():
    number = 0
    for element in file_list:
        print(element)
        number += 1
        numbero = str(number)
        m = os.path.splitext(element)
        os.rename(f'{folder}{element}', f'{folder}{numbero}{m[1]}')

    file_list2 = os.listdir(folder)
    print(file_list2)


def enumerate_name():
    print(' Enter the file name you want to use for renaming your files.')
    pattern_name = input('Enter name: ')
    number = 0
    for element in file_list:
        print(element)
        number += 1
        numbero = str(number)
        m = os.path.splitext(element)
        os.rename(f'{folder}{element}', f'{folder}{numbero}{pattern_name}{m[1]}')

    file_list2 = os.listdir(folder)
    print(file_list2)


def name_enumerate():
    print(' Enter the file name you want to use for renaming your files.')
    pattern_name = input('Enter name: ')
    number = 0
    for element in file_list:
        print(element)
        number += 1
        numbero = str(number)
        m = os.path.splitext(element)
        os.rename(f'{folder}{element}', f'{folder}{pattern_name}{numbero}{m[1]}')

    file_list2 = os.listdir(folder)
    print(file_list2)


folder = check_path()
file_list = os.listdir(folder)
print('')
print('------------------------------------')
print(f' Files in {folder}: \n {file_list} \n')


def choice_menu():
    print('How would you like to change the File names:')
    print('1. Enumerate')
    print('2. WORD and enumerate.')
    print('3. Enumerate and Word')
    while True:
        try:
            choice = int(input('>> '))
            if choice in range(1, 4):
                return choice
            print('Choose between 1 -3. Try again')

        except ValueError:
            print('Wrong. Enter the number.')
            pass


choices = choice_menu()


if choices == 1:
    enumeration()
elif choices == 2:
    name_enumerate()
elif choices == 3:
    enumerate_name()
