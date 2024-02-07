f = open("main1.txt")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())


f = open("main1.txt")
print(f.readline())
f.seek(0)
print(f.readline())

f.close()





