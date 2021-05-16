from turtle import Turtle, Screen
import random
from bubbles import the_people


screen = Screen()
screen.setup(1500, 1500)
screen.bgpic("images/SKY-SPORTS.gif")
line = Turtle()

players = []
pictures = []

while len(players) < 6:
    player = Turtle()
    picture = f"Images/team_members_photos/{random.choice(the_people)}"
    while picture in pictures:
        picture = f"Images/team_members_photos/{random.choice(the_people)}"
    pictures.append(picture)
    screen.addshape(picture)
    player.shape(picture)
    players.append(player)


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

# starting positions
x = -600
y = -400
for i in players:
    i.speed("fastest")
    i.penup()
    i.goto(x, y)
    y += 150


def gameplay():
    m = True
    random.shuffle(players)
    while m:
        for i in players:
            if i.xcor() >= 600:
                m = False
            elif i.xcor() < 600:
                i.forward(random.randint(0, 25))


gameplay()

screen.exitonclick()