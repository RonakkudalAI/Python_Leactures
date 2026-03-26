
# keys() - Return All Keys
# values()- return all Values
# items()- return key-value pairs as tuple
# get(key)- a safer way to access value of a particular KeyboardInterrupt
#          Instead of Throwing an error it return None if Key doesn't exit.KeyError
# update(new_item)- adds a new iteam to the dictionary

d = {
    "Name": "Ronak",
    "Subject":["math","science","physics"],
    "cgpa":9.5
}

print(d.keys())
print(d.values())
print(d.items())
print(d.get("cgpa2"))
new_item = {"city":"Delhi"}
print(d.update(new_item))
print(d)

