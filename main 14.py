                #BREAK AND CONTINUE STEMENT

i = 0
"""
while(i<45):
    print(i+1, end=" ")
    i = i+1"""

"""
while(True):
    print(i+1, end=" ")
    if(i==44):
        break     #stope the loop
    i = i+1"""

"""
while(True):
    if i+1<5:
        i = i + 1
        continue
    print(i+1, end=" ")
    if(i==44):
        break     #stope the loop
    i = i+1"""


while(True):
    inp = int(input("enter a number\n"))
    if inp>100:
        print("you win")
        break
    else:
        print("try again!\n")
        continue