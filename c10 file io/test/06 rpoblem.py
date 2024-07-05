with open("test/06log.txt") as f:
    c=f.read()
    if "python" in c:
        print("found it ")
       
    else:
     print("not found")