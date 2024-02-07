# lists and list function
grocery = ["HARPIC" , "VIM BAR", "DEODRANT" ,"BHINDI" ," LOLLYPOP" , 56]
print(grocery)
print(grocery[0])
print(grocery[3])
print(grocery[5])

numbers=[2,7,9,11,3]
print(numbers)
print(numbers[3])    # 1

numbers.sort()
print(numbers)       # 2

numbers.reverse()
print(numbers)       # 3

"""
numbers=[]
numbers.append(71)
numbers.append(71)
numbers.append(71)
print(numbers) """    #4   ( append means joining in last of the list)

"""numbers.insert(2,37) numbers.insert(0 to 4, x)
print(numbers)"""     # 5


"""numbers.remove(11)
print(numbers)"""     # 5


"""numbers.pop()
print(numbers)"""     # 6 remove list of last element


numbers[1] = 77
print(numbers)        # 7

#MUTABLE=CAN CHANGE
#IMMUTABLE=CANOT CHANGE


"""tp = (1,2,3)  # how to make tapple
tp = (1)        #  tp = 8 ans error because of value of tuple is not change (immutable)
tp=(1,)         #   value of list is change (mutable)
print(tp)"""          # 8



a=1
b=7
a,b=b,a
#temp = a
#a = b
#b = temp
print(a,b)      # interchange of element


