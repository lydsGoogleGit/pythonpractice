from turtle import Turtle

XCOR_PLAYER = 800
XCOR_COMP = -800
UP_HEADING = 90
DOWN_HEADING = 270


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.p_paddle = Turtle("square")
        self.p_paddle.fillcolor("white")
        self.p_paddle.turtlesize(stretch_wid=1, stretch_len=7)
        self.p_paddle.goto(XCOR_PLAYER, 0)
        self.p_paddle.setheading(90)
        self.c_paddle = Turtle("square")
        self.c_paddle.fillcolor("white")
        self.c_paddle.turtlesize(stretch_wid=1, stretch_len=7)
        self.c_paddle.goto(XCOR_COMP, 0)
        self.c_paddle.setheading(90)

    def move_up(self):
        self.p_paddle.forward(50)

    def move_down(self):
        self.p_paddle.backward(50)