# Dictionary : Key :: Value Pair
student = {"name": "Amit",
           "Addr": "Mumbai",
           "Course": "AI" 
           }
print(student)

print(student["name"])
# Keys : int, flat,str, tuple, frozenset
# Not allowed : List, set Dictionary

# d = {[1,2]:"a"} 
# Type Error : Unhashable type : 'list'

# dict(): Dictionary Constructor

d = dict(a=1,b=2,c=3)
print(d)
print()

dic = dict([("a",1),("b",2),("c",3)])
print(dic)

keys = ["id", "name","addr"]
values = ["s1","Amit","Mumbai"]
d = dict(zip(keys,values))
print(d)
print(
    
)