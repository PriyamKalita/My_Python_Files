#try except exception handing in python

print("enter num 1")
num1 = input()
print("enter num 2")
num2 = input()
try:
    print("this sum of these two numbers is",
    int(num1)+int(num2))
except Exception as e:
    print(e)


    print("this line is very importent")


