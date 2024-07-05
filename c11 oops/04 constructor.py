class Employee:

    language="py" #this is a class attribute
    salary=120000
     

    def __init__(self,name,salary,language):  #dunder method which is automatically called
        self.name =name
        self.language=language
        self.salary=salary
        
        
        print("haseen is a good boy") 

    def getinfo(self):
        print(f"the language is {self.language}.the salary is{self.salary}")


    @staticmethod         
    def greet():
        print("good morning")




harry=Employee("haseen",130000,"hindi")
# harry.name="haseen"
print(harry.name,harry.salary,harry.language)



# haseen=Employee()

