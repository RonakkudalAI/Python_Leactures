list = [1,2,3,4,5,6,7,8,9,10]

print(list)

list.append(999)
print(list)

list.extend([55,66,77])
print(list)

list.append(1000)
print(list)
list.insert(10,555)
print(list)

list.pop()
print(list)
list.pop(0)
print(list)
list.pop(9)
print(list)
list.sort()
print(list)
# list.count()
# print(list)
list.copy()
print(list)
print(list.count(2))
print(len(list))
print(max(list))
print(min(list))