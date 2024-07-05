def f(l,c):
    n=[]
  
    for i in l:
        #  if('c'==l[c]):
        if not(i==c):
            n.append(i.strip(c))
    return n        
            
            # l.remove(c)
            # return l
             


l=["nhaseen","hellon","harsh","nSRE"]
c=input("enter ")
print(f(l,c))