def star(c):
   
    if(c==0):
       return 
    print("*"*c)
    star(c-1)

c=int(input("enter "))   
star(c)    