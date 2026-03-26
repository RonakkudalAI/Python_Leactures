# Lines = ["\nRonak","\nManali","\nKudal"]
# f.open("Day8/abc.txt","w")

import os

with open("Day8/abc.txt","r") as f:
    print(f.read())


with open("Day8/abc.txt","r") as f:
    print(f.tell()) # Starting Position = 0
    print(f.read(7))
    print(f.tell()) 
    
    f.seek(0)
    print(f.read())


if os.path.exists("Day8/abc.txt"):
            print("Yesss.........")
else:
         print("No...............")
print()

print(f.name)
print(f.mode)
print(f.closed)





try:
       with open("abc11.txt","r") as f:
              print(f.read())
except FileNotFoundError:
       print("Not Available")