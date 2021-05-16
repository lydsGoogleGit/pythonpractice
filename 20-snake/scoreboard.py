from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.intro_score()

    def intro_score(self):
        self.penup()
        self.color("green")
        self.hideturtle()
        self.goto(250, -250)
        self.write("Scoreboard", align="right", font=("arial", 12, "bold"))

    def game_over(self):
        self.penup()
        self.color("red")
        self.hideturtle()
        self.goto(0,0)
        self.write(f"GAME OVER", align= "center", font=("arial", 30, "bold"))

    def update_score(self, score):
        self.penup()
        self.color("blue")
        self.hideturtle()
        self.goto(250, -280)
        self.clear()
        self.write(score, align="right", font=("arial", 18,))