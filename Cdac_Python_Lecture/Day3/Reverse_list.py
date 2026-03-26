n = [12, 34, 67, 45, 14, 18, 1, 78, 65]
list = []


for num in range(len(n)-1,-1,-1):
    list.append(n[num])

print("Reverse",list)

print(n[::-1])

n.reverse()
print(n)

