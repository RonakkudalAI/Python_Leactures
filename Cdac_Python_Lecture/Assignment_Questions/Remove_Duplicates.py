nums = list(map(int, input("Enter list: ").split()))

unique = []

for n in nums:
    if n not in unique:
        unique.append(n)

print("List after removing duplicates:")
for n in unique:
    print(n, end=" ")