import string

s = string.ascii_lowercase

print(s)

b = [i for i in s]
print(b)

print(*b[1::2], sep=',')
#print(string[2::3])