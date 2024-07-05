a=int(input("enter the nimber "))
b=int(input("enter the nimber "))
if(b==0):
    raise ZeroDivisionError("hey our program not divide zero")
else:
   print(f"the division a/b is {a/b}")