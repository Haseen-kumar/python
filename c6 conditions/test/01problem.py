a=int(input("enter the number 1 :- "))
b=int(input("enter the number 1 :- "))
c=int(input("enter the number 1 :- "))
d=int(input("enter the number 1 :- "))

if(a>b and a>c and a>d ):
    print("the greatest number is ",a)

elif(b>a and b>c and b>d):
    print("the greatest number is ",b)

elif(c>a and c>b and c>d):
    print("the greatest number is ",c)

elif(d>a and d>c and d>b):
    print("the greatest number is ",d)

else:
    print("you enterd the same value of all idoit")