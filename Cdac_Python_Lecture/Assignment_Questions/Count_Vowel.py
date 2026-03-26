String = input("Enter the String You Want to count")
count = 0

for ch in string:
    if ch in 'aeiouAEIOU':
        count += 1
print(count)