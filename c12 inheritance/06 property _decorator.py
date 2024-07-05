class hello:
    a=23
    @classmethod
    def hi(cls):
        print(f"the class attribute is {cls.a}")

    @property
    def name(self):
        return f"{self.fname}   {self.lname}"
    
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
#uper wala system hi encapsulation and abstraction kehte hai
#hot akuch nhi sirf name split kr raha hai user ko bina batye



p=hello()
p.a=234
p.name='haseen kumar'
print(p.name)
print(p.fname,p.lname)

p.hi()
