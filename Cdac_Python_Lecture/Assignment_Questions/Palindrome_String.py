String = input("Enter The String :")

original = String

rev ="" 
for ch in String:
    rev = ch+rev
if(rev == original):
    print("String is Palindrome")
else:
    print("String is not Palindrome")