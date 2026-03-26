import datetime

# d1 = datetime.date(2026,3,21)
# d2 = datetime.date(2026,5,15)

# diff = d2-d1
# print(diff)


# today = datetime.date.today()
# f1 = today+datetime.timedelta(days=5)
# print(f1)

# f2 = today-datetime.timedelta(days=5)
# print(f2)




# today = datetime.date.today()
# birthday = datetime.date(2002, 4, 2)

# Days = today - birthday
# Age = Days.days // 365   # ✅ correct

# print("My Age is:", Age, "Years")


# deadline = datetime.date(2026,25,3)
# today = datetime.date.today()



#String to Date Format

date_str = "20-04-2026"
date = datetime.datetime.strptime(date_str,"%d-%m-%Y").date()
print(date)
