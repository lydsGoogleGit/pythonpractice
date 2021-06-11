from turtle import Turtle, Screen
import random
from players import Player, THE_PEOPLE
from forfeits import forfeits


screen = Screen()
screen.setup(1500, 1500)
screen.bgpic("images/peggs_at_races.gif")
line = Turtle()
winner = Turtle()

for image in THE_PEOPLE:
    screen.addshape(f"Images/{image}.gif")

screen.listen()
players = []
is_set =[]

while len(set(players)) < 6:
    player = Player()
    player.hideturtle()
    if player.person not in is_set:
        is_set.append(player.person)
        players.append((player.person, player))

# starting positions
x = -600
y = -400

for i in players:
    i[1].penup()
    i[1].speed("fastest")
    i[1].shape(f"Images/{i[0]}.gif")
    i[1].showturtle()
    i[1].goto(x, y)
    y += 150

# winner
winner.penup()
winner.color("green")
winner.hideturtle()
winner.goto(-400, -400)

# loser
loss = Turtle()
loss.penup()
loss.color("green")
loss.hideturtle()

# finish line
line.penup()
line.goto(600, -400)
line.left(90)
for i in range (20):
    line.width(20)
    line.color("white")
    line.speed("fastest")
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

# winner_guess = screen.textinput("Make your guess", f"Who will win the race?")


def gameplay():
    m = True
    while m:
        random.shuffle(players)
        for i in players:
            if i[1].xcor() >= 600:
                finishing_positions = {m[0]: m[1].xcor() for m in players}
                print(finishing_positions)
                key_list = list(finishing_positions.keys())
                val_list = list(finishing_positions.values())
                loser_xcor = val_list.index(min(val_list))
                loser = key_list[loser_xcor]
                print(loser)
                winner.goto(-300, 0)
                winner.write(
                    f"{i[0]} is the winner!",
                    move=False, align="center", font=("Courier New", 50, "bold"))
                print(i)
                loss.goto(-300, -100)
                loss.color("red")
                loss.write(
                    f"{loser} is the loser!",
                    move=False, align="center", font=("Courier New", 50, "bold"))
                loss.goto(-300,200)
                loss.color("white", "blue")
                loss.write(
                    f"Forfeit:\n{random.choice(forfeits)}",
                    move=False, align="center", font=("Courier New", 50, "bold"))
                m = False
                break
            elif i[1].xcor() < 600:
                i[1].forward(random.randint(0, 25))


gameplay()

screen.exitonclick()