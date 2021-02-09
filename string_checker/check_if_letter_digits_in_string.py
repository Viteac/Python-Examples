

text='1 2 3 4'

import string

li = text.split()

true = all(i.isdigit() for i in li)
if not true:
    if any(k in string.ascii_letters for k in li):
        print('There is a letter')
else:
    print('Only numbers')
