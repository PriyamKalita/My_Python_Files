#USING WITH BLOCK TO OPEN PYTHON FILES

f = open("main1.txt","rt")
print(f.readline())
print(f.readline())
f.close()

with open("main1.txt") as f:
    a = f.readlines()
    print(a)


