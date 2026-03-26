#Largest of 3 number is :
def get_largest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c
print(get_largest(3,4,10))