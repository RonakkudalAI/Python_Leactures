list1 = list(map(int,input("Enter the first list elements :").split()))
list2 = list(map(int, input("Enter the Second list of element").split()))

mergered_list = list1+list2
mergered_list.sort()

print(f"sorted merge list is :{mergered_list}")