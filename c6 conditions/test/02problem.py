a=int(input("enter the total marks :- "))
b=int(input("enter the subject 1 :- "))
c=int(input("enter the subject 2 :- "))
d=int(input("enter the subject 3  :- "))
s=100


if((b/s)*100>=33 and (c/s)*100>=33 and (d/s)*100>=33 ):
    print("you passed all subjetcs idoit ")
    if((b+d+c/a)>=40):
        print("you are promoted to next class")
    else:
        print("sorry you are not promoted to next class")
    
else:
    print("you are failed in sunject already")
