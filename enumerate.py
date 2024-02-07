"""
l1 = ("bhindi", "aloo", "chopsticks", "chowein")

i = 1
for item in l1:
    if i%2 != 0:     #!= mean not equal
        print(f"jarvis please buy {item}")
    i += 1"""

l1 = ("bhindi", "aloo", "chopsticks", "chowein")

for index , item in enumerate(l1):
    if index%2==0:
        print(f"jarvis please buy{item}")

