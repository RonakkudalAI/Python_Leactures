num = int(input("Enter the Number :"))

for i in range(0, num):
    for j in range(num-i,0,-1):
        print("*",end=" ")
    print()