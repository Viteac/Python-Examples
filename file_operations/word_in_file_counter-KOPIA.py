
with open('words.txt', 'r') as f:
    read = f.read()
words = read.lower().split()

for word in words:
    if word.endswith(',') or word.endswith('.'):
        words[words.index(word)] = word.rstrip(",.")

print(f'Words in a file: \n {words}')

counted = {}
limax = []
limin = []
for word in words:
    s = words.count(word)
    counted[word] = s

sort_orders = sorted(counted.items(), key=lambda x: x[1], reverse=True)
key_list = list(counted.values())
key_list = sorted(key_list)
min_val = key_list[0]
max_val = key_list[-1]

for element, val in counted.items():
    if val == min_val:
        limin.append(element)
    elif val == max_val:
        limax.append(element)
print(f"Most common occurs {max_val}: \n {','.join(limax)} ")
print(f"Least common occurs {min_val}: \n {','.join(limin)}")
