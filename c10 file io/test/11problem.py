with open("test/rename.txt") as f:
    c=f.read()

    with open("test/new renamed.txt","w") as f:
                        f.write(c) 