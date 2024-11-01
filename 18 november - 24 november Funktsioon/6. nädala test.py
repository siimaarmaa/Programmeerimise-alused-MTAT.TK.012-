from turtle import *

def ruut(kulg):
    for i in range(4):
        forward(kulg)
        left(90)

for i in range(10, 15):
    ruut(i)
    penup()
    forward(30)
    pendown()

exitonclick()