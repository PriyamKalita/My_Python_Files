                    # for loops

list1 = ["harry","larry","carry","marie" ]

for item in list1:
    print(item)              #1

list1 = [["harry", 1], ["larry", 2], ["carry", 3], ["marie", 5]]

for item in list1:
    print(item)              #2

list1 = [["harry", 1], ["larry", 2], ["carry", 3], ["marie", 5]]

for item ,lollypop in list1:
    print(item,lollypop)     #3

list1 = [["harry", 1], ["larry", 2], ["carry", 3], ["marie", 5]]

for item, lollypop in list1:
    print(item,"and lolly is",lollypop)      #4

list1 = [["harry", 1], ["larry", 2], ["carry", 3], ["marie", 5]]

dict1 = dict(list1)
print(dict1)               #5


item = {int, float, "harry", 5,3,3,44,65,77,79,23,21}

for item in item:
    if str(item).isnumeric() and item>9:
        print(item)        # 6


