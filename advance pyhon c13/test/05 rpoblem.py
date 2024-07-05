n=int(input("enter the no u want to table "))
table=[n*i for i in range(1,11)]


with open("test/tables.txt","a") as f:
    f.write(str(table)+"\n")