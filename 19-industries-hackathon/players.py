from turtle import Turtle
import random
THE_PEOPLE = ['ndiotto', 'janirudh', 'tanminh', 'dnorcott', 'vishalgoswami', 'koennecker', 'wutwin', 'coriehawkins', 'andrewcrisp', 'laylabennett', 'kdemczenko', 'ollyrichards', 'sofiadanko', 'divyasampath', 'lydiaart', 'sfreiberger', 'ndonko', 'louisedadey', 'andrew', 'worstenholme', 'butterly', 'ramanmadan', 'chenzuo', 'sanzpaul', 'attilaszabo', 'judeharrison', 'mjtierney', 'stavrosdenaxas', 'kdavidwang', 'vasugupta']


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.player = Turtle()
        self.person = random.choice(THE_PEOPLE)
