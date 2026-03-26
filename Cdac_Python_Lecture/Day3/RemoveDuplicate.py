n = [12,34,67,45,14,18,12,18,1,34,78,65]

list =[]

for num in n:
    if num not in list:
        list.append(num)
print("Unique list", list)