n=int(input("enter"))
for i in range(2,n): #here whun we give 2 no. is not included as n=2ao it will b=be excluded
    if(n%i==0):
        print("no is not prime")
        break

else:
    print("number is prime")

  