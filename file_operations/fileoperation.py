# Operation on file kaczka.txt

poem = open('kaczka.txt') #Opening file

print(poem.read()) #Printing the file

k = ["adamski", "pieszego"]
print(k)



for item in k:
    with open('kaczka.txt', "a") as f:
        f.write(item + "\n")
        f.close()

with open('kaczka.txt', "r") as m:
    print(m.read())
