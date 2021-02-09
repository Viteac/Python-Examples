import os


def checker(n):
    word = input('Enter the word to find\n >> ')
    this_line = 0
    words = 0
    find = word
    with open(n, 'r') as f:
        read_data = f.readlines()
        last = read_data[-1]

    for line in read_data:
        this_line += 1
        line = line.rstrip('\n')

        if find in line:
            if len(find) == len(line):
                words += 1
                print(f' {find} is in line {this_line}')
                if read_data is last:
                    break

    print('--------------------------------')
    if words == 0:
        print(f' No {find} in {n}.')
    elif words == 1:
        print(f'{find} appears {words} time in {n}')
    else:
        print(f'{find} appears {words} times in {n}')



def file_check():
    while True:
        file_name: str = input('Enter the file name \n >> ')
        m = os.getcwd()
        if os.path.isfile(m+'//'+file_name) is True:
            return file_name
        print(f' There\'s no a {file_name} in your directory\n Try again')


print('--------------------------')
print('|   <<< Word Finder >>>   |')
print('--------------------------')
file = file_check()
checker(file)
