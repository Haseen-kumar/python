class hello:
      a=10





h=hello()
print(h.a)  #prints the class attribute because instance attribute id=s not present
h.a=2000  # instance attribute is ser
print(h.a) #prints the instance attribute bexause instance attribute is present
print(hello.a)  #prints the class attribute