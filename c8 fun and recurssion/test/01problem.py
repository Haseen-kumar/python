def greatest():
    a=int(input("enter the no  "))
    b=int(input("enter the no  "))
    c=int(input("enter the no  "))

    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
    else:
        return ("idoit you are putting same value")
    

print(greatest(),"the greatest vaue is ")

    