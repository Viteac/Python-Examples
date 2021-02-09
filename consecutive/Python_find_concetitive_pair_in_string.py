import timeit
# run1 = '''

s = 'aabskaaaabadcccc'


lil = tuple(set(s))  # Set a characters in s to remove duplicates and then make a tuple
p = len(lil)


# list for counted repeats, the index of number repeats for character
# will be equal to index of its character in a tuple
li = [0 for i in range(p)]

for i in lil:    # iter over tuple of letters
    c = 0        # counter
    h= lil.index(i)  # take an index
    for letter in s:            # iterate ove the string characters
        if letter == i:         # check if equal with character from tuple
            c += 1              # if equal Counter +1
            if c > li[lil.index(letter)]:   # Updated the counter if present is bigger than the one stored.
                li[lil.index(letter)] = c
        else:
            c=0
            continue

m = max(li)

for index, j in enumerate(li):              # Check if the are characters with same max value
    if li[index] == m:
        print(f'{lil[index]} appears {m} consecutive times')


# '''
# print(timeit.timeit(stmt=run1, number=1))

