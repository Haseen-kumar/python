def generatetable(n):
    table=""
    for i in range(1,11):
        table +=f"{n} * {i} ={n*i}\n"

    with open(f"test/table/tables_{n}.txt","w") as f:
        f.write(table)


for i in range(2,21):
    generatetable(i)