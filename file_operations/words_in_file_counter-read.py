from collections import Counter
with open('words.txt', 'r') as f:
    read = f.read()
words = read.lower().split()  # load the file with words to count, lowercase them and create a list.

for word in words:   # Strip the words of punctuation
    if word.endswith(',') or word.endswith('.'):
        words[words.index(word)] = word.rstrip(",.")
print(f'Words in a file: \n {words}')
counterstrike = Counter(words)
print (counterstrike)
sort_orders = sorted(counterstrike.items(), key=lambda x: x[1], reverse=True)  # list with sorted items

key_list = list(counterstrike.values())  # list with sorted values
key_list = sorted(key_list)


min_val = key_list[0]
# min  and max values (min first element, max last one)
max_val = key_list[-1]


limax = []
limin = []
for element, val in counterstrike.items():
    if val == min_val:                 # add element meeting min condition to least list
        limin.append(element)
    elif val == max_val:                   # add element meeting max condition to max list
        limax.append(element)
print(f"Most common appeared {max_val} times: \n {','.join(limax)} ")
print(f"Least common appeared {min_val} time: \n {','.join(limin)}")
