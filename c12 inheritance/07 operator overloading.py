class number:
    def __init__(self,n):
        self.n=n

    def __add__(self,num):
        return self.n + num.n


n=number(4)
m=number(24)
p=number(24)
print(n+m)