#RECURSION:RECURSIVE VS ITERATIVE APPROACH
"""def print2(str1):
    print("this is"+str1)
print2(" parry") """ #recurstion mean using function inside a function

#n! = n*n-1*n-2*n-3.............1
#n! = n*(n-1)!

def factorial(n):
    """:param n: Integer
    :return: n*n-1*n-2*n-3......"""
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


    pass
number = int(input("enter then number"))

print(factorial(number))




