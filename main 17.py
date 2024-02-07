         #function and docstrings

"""a = 9
b = 7
c = sum((a,b))    #bulid in function
print(c)"""

"""def funtion1 (a,b):
    print("hello you are in function",a+b)

    def function2(a,b):
        averge = a+b/2
        return averge
    v = function2(5,7)
    print(v)"""


def function1 (a, b):
    print("hello you are in function1", a+b)

    def function2(a, b):
        """This is a function which will
        calculate average of two number"""
        average = a+b/2
        #print average
        return average

#v = function(5,7)
    #print(v)

    print(function2.__doc__)












