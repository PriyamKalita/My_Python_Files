#python file IO basics
"""
"r" - open file for reading -default
"w" - open a file for writing
"x" - creates file if not exists
"a" - add more content to a file
"t" - text mode - default
"b" - binary mode
"+" - read and write
"""

f = open("main.txt")
content = f.read()
print(content)
f.close()    #1

f = open("main.txt","rt")
content = f.read(3)
print(content)

content = f.read(3)
print(content)
f.close()     #2

f = open("main.txt","rt")
print(f.readline())
print(f.readline())
print(f.readline())






