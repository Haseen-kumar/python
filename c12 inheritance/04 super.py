class employee:
    def __init__(self):
        print("hello employee")
    a=1

   

class progrmmer(employee):
    def __init__(self):
        print("hello  programmer")
    b=2

class manager(progrmmer):
    def __init__(self):
        super().__init__()
        print("hello manager")
    
    c=3


p=manager()
# p.a="hello"
print(p.a)
print(p.b,p.c)

# o=progrmmer()
# print(o.c)  #showa an error because multilevel 