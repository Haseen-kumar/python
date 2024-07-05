
with open("test/06log.txt") as f:
    lines=f.readlines()
lineno =1
for line in lines: 
    if "python" in line:
        print("found it ")
        print(f"found it in line no. {lineno} ")
        break
        lineno += 1
else:
     print("not found")
    