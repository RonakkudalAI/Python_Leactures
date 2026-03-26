n = [12,34,67,45,14,18,12,18,1,34,78,65]

# for num in n:
#     print(num,":" , n.count(num))

for num in set(n):
    print(num, ":", n.count(num))