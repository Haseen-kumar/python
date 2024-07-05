def f(c):
     if(c==1):
        return 1
     else:
         return f(c-1)+c
c=int(input("enter the no. "))

print(f(c))

