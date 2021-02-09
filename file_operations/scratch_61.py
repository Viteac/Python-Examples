def checker(n):

    this_line = 0
    find = 'kogut'
    with open (file_name, 'r') as f:
        read_data = f.readlines()
    for line in read_data:
        this_line +=1
        if find in line:
            print (f' Your word  {find} is in line {this_line}')
file_name = 'ten_plik.txt'

checker(file_name)