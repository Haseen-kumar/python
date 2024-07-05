class employee:
    salary=234
    increment=20
    @property
    def salaryafterincrement(self):
        return  (self.salary+self.salary*(self.increment/100))
    
    
    @salaryafterincrement.setter
    def salaryafterincrement(self, salary): 
        self.increment=((salary/self.salary)-1)*100



p=employee()
print(p.salaryafterincrement)
p.salaryafterincrement=280.800000000001
print(p.increment)

#here () is not pred=sent in salaeryafterin bnecause of the property decorator