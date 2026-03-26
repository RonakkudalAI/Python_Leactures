try: 
    num = int(input("Enter the number:"))
    
    if num < 0:   
         raise ValueError("Negative number are not allowed")     

except ValueError as ve:
    print("Error",ve)

except Exception as e:
    print("Invalid input ",e)

else:
    print("valid number :",num)

finally:
    print("program ended:")
    
    
