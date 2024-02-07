#n! = n*n-1*n-2*n-3.............1
#n! = n*(n-1)!
def factorial_iterative(n):
    """:param n: Integer
        :return: n*n-1*n-2*n-3......"""
    fac = 1
    for i in range(n):
        fac = fac * (i +1)
    return  fac

def factorial_recursive(n):
    """:param n: Integer
        :return: n*n-1*n-2*n-3......"""
    if n == 1:
        return 1

    else:
        return n * factorial_iterative(n-1)




number = int(input("enter the number"))
print("factorial using iterative method", factorial_iterative(number))
print("factorial using recursive method", factorial_recursive(number))


#n! = n*n-1*n-2*n-3.............1
#n! = n*(n-1)!