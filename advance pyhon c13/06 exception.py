try:
   a=int(input("enter the nimber "))
   print(a)

except ValueError as v:
   print("hey")
   print(v)


except Exception as e:
   print(e)


print("thanku")
