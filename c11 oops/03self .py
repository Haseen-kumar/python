class Employee:

    language="py" #this is a class attribute
    salary=120000


    def getinfo(self):
        print(f"the language is {self.language}.the salary is{self.salary}")


    @staticmethod         
    def greet():
        print("good morning")




harry=Employee()
harry.language="javascript"

harry.getinfo() #only this shows an error
harry.greet()

#because it converted into
#both are correct

# Employee.getinfo(harry)

