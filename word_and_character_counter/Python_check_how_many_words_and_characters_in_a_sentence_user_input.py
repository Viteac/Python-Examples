import string

while True:
    while True:
        sentence = input('Enter a sentence:\n> ')
        if all(x not in string.punctuation for x in sentence):
            words = sentence.split()
            print(words)
            numbers = [len(x) for x in words]
            u= ','.join(str(x) for x in numbers)
            print(f'Your sentence has { len(words)} words. Each word has {u} number of characters.')
        else:
            print('Try again mate, no punctuation characters')
            pass

