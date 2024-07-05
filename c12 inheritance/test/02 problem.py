class animal:
    def method():
        print("bark animal")


class pet(animal):
    pass


class dog(pet):
    @staticmethod
    def bark():
        print("bark in the night dog")


d=dog()
d.bark()


