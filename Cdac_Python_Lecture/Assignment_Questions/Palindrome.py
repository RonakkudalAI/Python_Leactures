num = int(input("Enter the number "))
original = num
rev = 0

while(original != 0):
    digit = original % 10
    rev = rev * 10 + digit
    original = original // 10

if(rev == num):
    print(num, "is Palindrome")
else:
    print(num, "is not Palindrome")