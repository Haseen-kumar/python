
import random

def game():
      
      #point to be noted
      #read and write operation only on string or str


      r=random.randint(1,100)
      with open("test/hiscore.txt","r") as f:
            c=f.read()
           
                
            if(c!=""):
                    c=int(c)
            else:
                  c=0
            print(f"(your high score {r} vs previous {c})")
           
            if( r>c):
                  with open("test/hiscore.txt","w") as f:
                        f.write(str(r))
            else:
                  with open("test/hiscore.txt","w") as f: #write fun hamesha sting leta hai
                        
                        f.write(str(c))
                  






game()
