#writing and aooending to a file
"""
f = open ("main.txt","w")
a = f.write("hello world\n")
print(a)
f.close()"""

#handle read and write both
f = open("main.txt","r+")
print(f.read())
f.write("thank you")





