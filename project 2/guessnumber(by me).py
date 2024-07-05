import random
x=random.randint(1,10)
u=-1
guesses=1
while(x!=u):

  u=int(input("guess the number:-- "))

  if(u<x):
    print("greater number pls ")
    guesses+=1
  elif(u>x):
    print("lower number pls ")
    guesses+=1
  else:
    print("u are the perfect gusser bro ! ")

print(f"you have no. {x} in of guesses  {guesses}")
