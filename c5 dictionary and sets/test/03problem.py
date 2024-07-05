s={18,"18",18.0}
print(type(s),s,len(s))

r= set() 

r.add(20)
print(len(r)) 
r.add(20.0) 
print(len(r))
r.add('20')  #length of s after these operations? 
print(len(r))


p={}
print(type(p))