class Employee:
    # name="haseen"
    language="py" #this is a class attribute
    salary=120000

harry=Employee()
print(harry.salary,harry.language)    


haseen=Employee() 
haseen.language="c++"  #this is the object/instance attribute
print(haseen.salary,haseen.language)  



#instance attribute have preference over class attribute

#here object attribute and salary and language are class
#  attribute sas they directly belong to the class