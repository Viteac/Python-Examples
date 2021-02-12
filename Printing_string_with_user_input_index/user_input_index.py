s = 'Hello'

k = len(s)
ind = False

while not ind:
    try:
        ind = int(input('Index> '))
    except ValueError:
        print('Numbers only')
    if ind > k:
        print('wrong range, try again')
        ind = False


print(s[ind:])


