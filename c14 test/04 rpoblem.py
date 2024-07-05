def devidible5(n):
    if(n%5==0):
        return True
    return False

a=[43,554,65,7,6,8,554,64,534,234,2,3,4,3545,4,54,5,4,545]


f=list(filter(devidible5,a))

print(f)