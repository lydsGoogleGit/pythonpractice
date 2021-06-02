from turtle import Turtle, Screen
import random
from players import Player, THE_PEOPLE

screen = Screen()
screen.setup(1500, 1500)
screen.bgpic("images/SKY-SPORTS.gif")
line = Turtle()

for image in THE_PEOPLE:
    screen.addshape(f"Images/team_members_photos/{image}")


screen.listen()
# winner_guess = screen.textinput("Make your guess", f"Who will win the race? {ldap_string}")

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

players = []

while len(players) < 6:
    player = Player()
    players.append((player.person, player))


# starting positions
x = -600
y = -400

for i in players:
    i[1].penup()
    i[1].speed("fastest")
    i[1].shape(f"Images/team_members_photos/{i[0]}")
    i[1].goto(x, y)
    y += 150


def gameplay():
    m = True
    random.shuffle(players)
    while m:
        for i in players:
            if i[1].xcor() >= 600:
                print(i)
                m = False
            elif i[1].xcor() < 600:
                i[1].forward(random.randint(0, 25))


gameplay()

screen.exitonclick()