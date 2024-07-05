class claculator:

    def __init__(self,n):
        self.n=n
    

    def square(self):
        print(f"the square of {self.n} is {self.n*self.n}")

    @staticmethod
    def getname():
        print("hello ")
    
    def cube(self):
        print(f"the square of {self.n} is {self.n*self.n*self.n}")
    
    def sqr(self):
        print(f"the square of {self.n} is {self.n**1/2}")





p=claculator(4)
p.square()
p.cube()
p.sqr()
p.getname()

