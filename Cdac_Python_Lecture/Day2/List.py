list = [1,2,3,4,5,6,7,8,9,10]
print(list)
list.extend("CDAC")
print(list)
list.insert(0,200)
print(list)
list.remove(200)
print(list)
list.pop()
print(list)
list.pop(2)
print(list)

# list.clear()
# print(list)

del list[1]
print(list)