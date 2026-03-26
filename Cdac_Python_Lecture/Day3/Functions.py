# Functions:
# A function is a named, block of code that performs a specific task.
# It helps to avoid repetiton of code.
# It improve readability


def add(a,b):
    return a+b
print(add(11,22))

# Types of Arguments in Functions:
# 1. Positional Arguments 
# 2.keyword Arguments
# 3.Default Arguments
# 4.Variable Length arguments
# #-------------------------------------
# 1.Positional arguments:

# -The order of parameter is importanat
# Values  are assigned is according to their position

def sub(a,b):
    print(a-b)

sub(10,5)
add(5,10)

# 2.Keywords Arguments
# In Keyword arguments, the parameter name while passing the values
# -order doesnot matter.

def sub(a,b):
    print(a-b)
sub(a=10,b=5)
sub(b=10,a=5)

# Default Arguments
def greet(name="Test"):
    print("Hi",name)

greet("Amit")
greet()
# Variable Length arguments("arguements"):
# -used when the number of arguments is not known in advanced
# - args collects multiple values into a tuples

def sum(*n):
    s = 0
    for i in  n:
        s+=i
    print(s)
sum(10,20)
sum(10,20,30,40,50)

#  Return Statements:
# return used to send a value back from the functions
# -return one single 
# return  values
#  return nothing (none)

def sqr(a):
    return a*a
x = sqr(5)
print(x)
print(sqr(5))


# ------------------------------------------
def calc(a,b):
    return a+b,a-b,a*b
x,y,z = calc(10,20)
print(x,y,z)
# -------------------------------------------
# Recursive Functions: A recursive is a functions that call itself.
# 