num = int(input("Enter the number: "))

fib1 = 0
fib2 = 1

print(fib1)
print(fib2)

for i in range(2, num):
    fib = fib1 + fib2
    print(fib)
    fib1 = fib2
    fib2 = fib