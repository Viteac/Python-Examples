with open('file.txt') as f:
    read = f.readlines()
c = 0
for i, v in enumerate(read):
    v = v.rstrip('\n')
    read[i] = v
    c += 1
    b = v.split()
    words = len(b)

    if words == 1:
        print(f'Line {c}: Has {words} word and {len(v)} rows ')
    else:
        print(f'Line {c}: Has {words} words and {len(v)} rows ')
