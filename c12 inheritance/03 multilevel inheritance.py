class employee:
    a=1

class progrmmer(employee):
    b=2

class manager(progrmmer):
    c=3


p=manager()
# p.a="hello"
print(p.a)
print(p.b)

o=progrmmer()
print(o.c)  #showa an error because multilevel 