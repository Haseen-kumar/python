# with open("poems.txt") as f:
#      print(f.read())



f=open("test/p.txt")
c=f.read()
if "haseen" in c:
    print(" found it ")
else:
    print("not found")


f.close()
