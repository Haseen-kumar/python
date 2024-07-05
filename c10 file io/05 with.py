f =open("file.text")

print(f.read())

f.close()

#the same can be written like this::--

with open("file.txt") as f:
    print(f.read())

    #dont need to close seperately
