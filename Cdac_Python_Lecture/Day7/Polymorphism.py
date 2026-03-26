class A:
    def m1(self,a = None, b= None):
        if a is not None and b is not None:
            print(a+b)
        elif a is not None:
            print(a)
        else:print("Their is no argument present")
a1 = A()
a1.m1()
a1.m1(18)
a1.m1(10,23)