from turtle import Turtle, Screen
import random
from players import Player, THE_PEOPLE

screen = Screen()
screen.setup(1500, 1500)
screen.bgpic("images/SKY-SPORTS.gif")
line = Turtle()
score = Turtle()

for image in THE_PEOPLE:
    screen.addshape(f"Images/team_members_photos/{image}.gif")


screen.listen()
players = []
is_set = []

while len(set(players)) < 6:
    player = Player()
    if player.person not in is_set:
        is_set.append(player.person)
        players.append((player.person, player))

# starting positions
x = -600
y = -400

for i in players:
    i[1].penup()
    i[1].speed("fastest")
    i[1].shape(f"Images/team_members_photos/{i[0]}.gif")
    i[1].goto(x, y)
    y += 150

score.penup()
score.hideturtle()
score.goto(-400, -400)
score.write(f"The players are: {players[0][0]}, {players[1][0]}, {players[2][0]}, {players[3][0]}, {players[4][0]}, {players[5][0]}",
            move=False, align="left", font=("Arial", 20, "normal"))

winner_guess = screen.textinput("Make your guess", f"Who will win the race?")

# finish line
line.penup()
line.goto(600, -400)
line.left(90)
for i in range (40):
    line.speed("fastest")
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)


def gameplay():
    m = True
    random.shuffle(players)
    while m:
        for i in players:
            if i[1].xcor() >= 600:
                score.goto(0,0)
                print(i)
                m = False
            elif i[1].xcor() < 600:
                i[1].forward(random.randint(0, 25))


gameplay()

screen.exitonclick()