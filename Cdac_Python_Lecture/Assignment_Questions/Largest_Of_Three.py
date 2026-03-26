a = int(input("Enter the first"))
b = int(input("Enter the Second"))
c = int(input("Enter the Third"))

if(a > b & a >c):
    print(a, "is Greater then all")
elif(b>c & b>a):
    print(b, "is Greater then all")
else:
    print(c,"is Greater then all")