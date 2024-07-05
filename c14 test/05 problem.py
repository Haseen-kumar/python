from functools import reduce

a=[43,5424,65,7,6,8,54,65]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,a))