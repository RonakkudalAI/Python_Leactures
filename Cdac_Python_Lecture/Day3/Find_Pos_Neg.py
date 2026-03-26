list = [1,2,3,4,5,6,-1,-1,-2,-5,-10]
list1 = []
list2 = []
for i in list:
    if(i >= 0):
        list1.append(i)
    else:
        list2.append(i)
        
print("positive number: ",list1)
print("Negative number: ",list2)