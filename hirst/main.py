# import colorgram
#
# extract = colorgram.extract('image.jpeg', 30)
# colours =[]
#
# for i in extract:
#     rgb = i.rgb
#     colours.append((rgb.r, rgb.g, rgb.from turtle import Turtle,
import random

colour_list = [(238, 243, 250), (235, 224, 84), (113, 179, 212), (213, 158, 111), (205, 5, 68), (235, 50, 128), (195, 74, 16), (194, 165, 12), (13, 22, 60), (31, 103, 167), (233, 225, 4), (28, 191, 119), (215, 135, 177), (17, 28, 173), (203, 31, 129), (230, 166, 199), (12, 184, 214), (119, 192, 162), (61, 22, 9), (35, 136, 76), (139, 219, 202), (9, 48, 26), (104, 92, 211), (188, 16, 5), (128, 218, 232), (238, 66, 36), (64, 12, 37)]


import turtle
turtle.colormode(255)
tim = turtle.Turtle()
tim.pensize(15)


def row():
    for _ in range(10):
        colour = random.choice(colour_list)
        tim.color(colour)
        tim.dot()
        tim.penup()
        tim.fd(70)


def left_turn():
    tim.left(90)
    tim.forward(70)
    tim.left(90)
    tim.forward(70)


def right_turn():
    tim.right(90)
    tim.forward(70)
    tim.right(90)
    tim.forward(70)


tim.penup()
tim.setpos(-320, -320)

for _ in range(5):
    row()
    left_turn()
    row()
    right_turn()




screen = turtle.Screen()
screen.exitonclick()
