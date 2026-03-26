salary = int(input("Enter your Salary : "))
if(salary < 30000):
    rate = salary*0.05
elif(salary == 30000 and salary == 70000):
    rate = salary*1.5
else:
    rate = salary *2.5

print(rate)


