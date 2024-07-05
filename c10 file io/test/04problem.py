p="donkey"
    
with open("test/04.txt") as f:
        c=f.read()

c=c.replace(p,"#####")
   
with open("test/04.txt","w") as f:
        f.write(c)



     


            