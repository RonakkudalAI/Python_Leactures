# Printing Methods in  Pythons:

# 1. Using Comma(,)
name = 'Ronak'
sal = 100000000000
print("Name = ",name,"sal = ",sal)



# 2 Using Operator +
print("Name = "+name)

#Method 3 Using % 
print("Name = %s and salary =%d" %(name,sal))

price = 1222.25841
print("price = %f" % price)
print("price = %.5f" % price)

#Using format()
print("Name = {0},  Salary = {1}".format(name,sal))
print("Name = {n},salary ={s}".format(n="Rahul",s=20000))

# Using f-String()
print(f"My name is {name} and salary is {sal}")

x =12365448.1541584
print(f"{x: .2f}")
print(f"{sal:10}")
print(f"{sal:<10}")
print(f"{sal:>10}")
print(f"{sal:^10}")
print(f"{sal:,}")