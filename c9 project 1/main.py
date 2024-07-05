'''
1 for snake 
-1 for water
0 for game
'''
import random
computer= random.choice([-1,0,1])
youstr =input("enter your choice ")
youdict={ "s":1,
          "w":-1,
          "g" :0}
reversedict={ 1:"snake",
          -1:"water",
          0:"gun" }
you= youdict[youstr]
#by now we have two numbers(variables) computer and you

print(f"computer :--  {reversedict[computer]} \n your:--  {reversedict[you]}")






if(computer== you):
     print("its a draw")
# else:
#       if(computer ==-1 and you==1):
#           print("you win")
#       elif(computer ==-1 and you == 0):
#         print("computer win")
#       elif(computer ==1 and you==-1):
#         print("computer win")
#       elif(computer ==1 and you==0):
#          print("you win")
#       elif(computer ==0 and you==1):
#          print("you win")
#       elif(computer ==0 and you==-1):
#         print("computer win")      

#       else:
#        print("something went wrong") 


#abovbe code also working 
#by the following code we reduce our lines of code by the readability decreases no new member can understand it properly



else:
     if((computer - you)== 1  or -(computer - you)== -2):
        print("you win")
     else:
        print("you lost")