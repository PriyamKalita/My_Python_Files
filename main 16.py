#             #short hand if else notation i python
# 
# a = int(input("enter a\n"))
# b = int(input("enter b\n"))
# 
# #if a>b: print("a is greter than b")
# 
# print("b > a") if a < b else print("a<b")
# 
# 
# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x//100 + 1)
	t.forward(x)
	t.left(59)
