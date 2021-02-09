with open('lines_written', 'r') as f:
    reader = f.read()

print(reader)


data = ['b1\n', 'b2\n', 'b3\n']

with open('lines_written', 'a') as f:
    f.writelines(data)


with open('lines_written', 'r') as f:
    reader = f.read()

print(reader)
