words=["from","hello","i"]


with open("test/05.txt") as f:
    c=f.read()

for word in words: 
      c=c.replace(word,"#" *len(word))

with open("test/05.txt","w") as f:
    f.write(c)