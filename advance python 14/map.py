#map examole
from functools import reduce
l=[1,2,4,5,4,6]



square =lambda x:x*x


sqlist=(map(square,l))
print(list(sqlist))

#filter example
def even(n):
    if(n%2==0):
        return True
    return False 
onlyeven= filter(even,l)
print(list(onlyeven))

#reduce example
def sum(a,b):
    return a+b

mul =lambda x,y:x*y

print(reduce(sum,l))
print(reduce(mul,l))