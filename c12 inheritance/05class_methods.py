class hello:
    a=23
    def hi(self):
        print(f"the class attribute is {self.a}")


p=hello()
p.a=35346
p.hi()


#if we wnat to call the cass attribute insted of instance attribute




class hello:
    a=23

    @classmethod
    def hi(cls):
        print(f"the class attribute is {cls.a}")


p=hello()
p.a=35346
p.hi()
