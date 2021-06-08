from turtle import Turtle
import random
THE_PEOPLE = ["Val", "Paddy", "Martyn", "Lek", "Poppy", "Hils"]

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.player = Turtle()
        self.person = random.choice(THE_PEOPLE)
        self.player.hideturtle()
