class twovector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"the vector are {self.i}i  and {self.j}j")


class threevector(twovector):
    def __init__(self,i,j,k):
          super().__init__(i,j)
          self.k=k 
     
    def show(self):
        print(f"the vector are {self.i}i  and {self.j}j and {self.k}k")



d=twovector(3,4)
d.show()
f=threevector(6,4,5)
f.show()