String = input("Enter String :")

# revString = String[::-1]
# print(revString)
rev =""
# Hello
for ch in String:
    rev=ch+rev
print("Reverse String : ",rev)