with open('lines_written', 'r') as f:
    reader = f.read()

print(reader)

#output:
This line was here already

Process finished with exit code 0


Process finished with exit code 0


data = ['b1\n', 'b2\n', 'b3\n']

with open('lines_written', 'a') as f:
    f.writelines(data)


with open('lines_written', 'r') as f:
    reader = f.read()

print(reader)

#output:
This line was here already
b1
b2
b3


Process finished with exit code 0
