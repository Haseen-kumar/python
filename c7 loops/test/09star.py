a=int(input("enter tne number :-- "))
for i in range(1,a+1):
      if(i==1 or i==a):
            print("*"*a)
      else:
            print("*",end="")
            print(" "*(a-2),end="")
            print("*")
    
     