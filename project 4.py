#project 4
#pattern printing
#input = integer n
#boolean = true or false
#
#true n = 5
# *
# * *
# * * *
# * * * *
#
#false n = 5
# * * * *
# * * *
# * *
# *

print("pattern printing")
num = int(input("enter num how many rows you want :"))
print("enter 1 or 0")
bool_val = input("1 for true value or 0 for false :")
if bool_val=="1":
    for i in range(0,num+1):
        print("*"*i)
if bool_val=="0":
    for i in range(num,0,-1):
        print("*"*i)             #1


a = int(input("please add number of the line you want to print"))
b = bool(int(input("please add 0 for false")))


def star(a,b):
    if b == True:
        c = 1
        while c <= a:
            print(c * "*")
            c = c + 1
    else:
        while a > 0:
            print(a * "*")
            a = a -1


star(a,b)


