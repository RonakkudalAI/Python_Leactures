# f = open("Day8/Student_Information.txt","r")
# print(f.read())
# f.close()

# f = open("Day8/Student_Information.txt","w")
# f.write(f"\n Name = Manali ")
# f.close()


f = open("Day8/Student_Information.txt","w")
data = f.write("Learn Python with Ronak")
print("Characters =",data)
print()
f.write("Learn New Tech")
f.write("Learn Ml")
f.write("learn Dl")
f.close()
