class UnderAgeException(Exception):
    pass
try:
    age = int(input('Enter your Age:'))
    if age <18:
        raise UnderAgeException("You are Under Age My Bro!!")

except UnderAgeException as ue:
    print("Error",ue)

except ValueError as ve:
    print("Invalid value",ve)

except Exception as e:
    print("Daya kuch to Gadbad hai...",e)

else:
    print("Are Bhai aap to bde ho Vote kro......")

finally:
    print("Duniya jaae Bhad me Hm to chlenge hi....")