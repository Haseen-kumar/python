def myfunc():
    print("hello world")

myfunc()


# print(__name__)



if __name__ =="__main__":
    #if this code is executed by running the  the file its present in
   print("we directly running this code")
   myfunc()
   print(__name__)
