from turtle import Screen
from paddle import Paddle

# creating the screen to look like the game

screen = Screen()
screen.bgcolor("black")
screen.setup(1750, 1000)

# create paddle
p_paddle = Paddle()

# get key presses to move the paddle

screen.listen()
game_on = True
screen.onkey(fun=p_paddle.move_up, key="Up")
screen.onkey(fun=p_paddle.move_down, key="Down")

while game_on:
    p_paddle.forward(50)




















screen.exitonclick()