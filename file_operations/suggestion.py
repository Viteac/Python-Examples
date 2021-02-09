find = 'kogut'
with open ('ten_plik.txt', 'r') as f:
    for line_number, line_contents in enumerate(f, 1):
        if find in line_contents:
            print (f' Your word  {find} is in line {line_number}')
            break
    else: # reached the end without breaking
        print(f' There is no word: {find} in your file.')
