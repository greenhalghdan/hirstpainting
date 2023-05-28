# import colorgram
# num = colorgram.extract("download.jpeg", 900)
# rgb_colors = []
# for i in num:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34), (11, 97, 52), (169, 181, 232), (241, 169, 155), (252, 7, 40), (10, 84, 100), (63, 98, 8), (14, 51, 250), (250, 11, 8)]

from turtle import Turtle, Screen
import random
import turtle
hirst = Turtle()
hirst.penup()
hirst.setposition(-300, -300)
# hirst.forward(10)
# hirst.dot(10)
turtle.colormode(255)
height = -300
hirst.speed(1000)
while height < 100:
    hirst.setposition(-300, height)
    for _ in range(0, 30):
        hirst.forward(20)
        hirst.pendown()
        #hirst.pencolor(random.choice(color_list))
        hirst.dot(10, random.choice(color_list))
        hirst.penup()
    height += 20
myscreen = Screen()
myscreen.exitonclick()