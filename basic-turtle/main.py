import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

#
#
# def square():
#     for i in range(4):
#         tim.forward(100)
#         tim.right(90)
#
#
# def dash():
#     for i in range(10):
#         tim.forward(10)
#         tim.up()
#         tim.forward(10)
#         tim.down()
#
#
# def big_shape():
#     colour = ["red", "purple", "green", "pink", "yellow", "blue", "cyan"]
#     sides = 3
#     total_angle = 180
#     turn_angle = total_angle - (total_angle / sides)
#     for i in range(sides):
#         print("triangle")
#         tim.forward(50)
#         tim.right(turn_angle)
#     sides += 1
#     total_angle += 180
#     for i in range(sides):
#         print("square")
#         turn_angle = (total_angle / sides)
#         tim.forward(50)
#         tim.right(turn_angle)
#     sides += 1
#     total_angle += 180
#     for _ in range(2):
#         turn_angle = total_angle - (total_angle / sides)
#         for i in range(sides):
#             tim.forward(50)
#             tim.right(turn_angle)
#         sides += 1
#         total_angle += 180
#
#
# def try_two():
#     colour = ["red", "purple", "green", "pink", "yellow", "cyan"]
#     sides = 3
#     for i in range(10):
#         exterior_angle = 360 / sides
#         tim.color(random.choice(colour))
#         for _ in range(sides):
#             tim.forward(100)
#             tim.right(exterior_angle)
#         sides += 1
#
#
turtle.colormode(255)
#
#


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
#
#
# def random_walk():
#     tim.pensize(10)
#     tim.speed(7)
#
#     def turn_left():
#         tim.left(90)
#
#     def turn_right():
#         tim.right(90)
#
#     def backwards():
#         tim.back(50)
#
#     def forwards():
#         tim.forward(50)
#
#     for _ in range(100):
#         tim.color(random_colour())
#         options = [turn_left, turn_right, backwards, forwards]
#         random.choice(options)()
#
#
# random_walk()
#
#


tim.speed(100)


def spirograph():
    heading = 5
    for _ in range(72):
        tim.color(random_colour())
        tim.circle(100, 360)
        tim.setheading(heading)
        heading += 5


spirograph()


screen = Screen()
screen.exitonclick()


