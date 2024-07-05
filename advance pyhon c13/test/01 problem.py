
try:
    with open("test/file1.txt","r") as f:
       print(f.read())
except Exception as e:
    print(e)

try:
    with open("test/file2.txt") as f:
     print(f.read())
    
except Exception as e:
    print(e)


try:
    with open("test/file3.txt") as f:
     print(f.read())

except Exception as e:
    print(e) 

print("thanku")    
    