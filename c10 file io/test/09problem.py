with open("test/08this.txt") as f:
    c=f.read()
with open("test/08tt.txt") as f:
        v=f.read()

if (c==v):
  print("identical")
else:
     print("not same")
    
