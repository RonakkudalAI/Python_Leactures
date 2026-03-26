# # In a shop their is a product and the unit of product is 7
# #if a person buy a product more then one time it gives 40% of discount on prices
# unit_price = 7
# quantity = int(input("Enter the number you want to Buy"))
# total = price * discount

# if quantity > 1:
# discount = total *0.40




Exp = int(input("Enter the Experience of Employee"))
performance_rating = int(input("Enter the Performance Rating of Employee"))
salary = 10000
if Exp >= 5 & performance_rating  >=4 :
    bonus = 10000*0.04
    print(bonus)
elif Exp >=4 & performance_rating >=3:
    bonus = salary*0.04
    print(bonus)
else:
    print("No Incremet")











