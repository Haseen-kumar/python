class Employee:
    # name="haseen"
    language="py" #this is a class attribute
    salary=120000

harry=Employee()
print(harry.salary,harry.language)    


haseen=Employee() 
haseen.name="haseen kumar"  #this is the object/instance attribute
print(haseen.name,haseen.salary,haseen.language)  


#here object attribute and salary and language are class
#  attribute sas they directly belong to the class