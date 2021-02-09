li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
string='abcdefghijklmnoprstuwxyz'
start = 1

for i in string:
    if string.index(i) == start:
        print(i)
        start += 2

