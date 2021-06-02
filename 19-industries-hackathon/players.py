from turtle import Turtle
import random
THE_PEOPLE = ['ndiotto.gif', 'janirudh.gif', 'tanminh.gif', 'dnorcott.gif', 'vishalgoswami.gif', 'koennecker.gif', 'wutwin.gif', 'coriehawkins.gif', 'andrewcrisp.gif', 'laylabennett.gif', 'kdemczenko.gif', 'ollyrichards.gif', 'sofiadanko.gif', 'divyasampath.gif', 'lydiaart.gif', 'sfreiberger.gif', 'ndonko.gif', 'louisedadey.gif', 'andrew.gif', 'worstenholme.gif', 'butterly.gif', 'ramanmadan.gif', 'chenzuo.gif', 'sanzpaul.gif', 'attilaszabo.gif', 'judeharrison.gif', 'mjtierney.gif', 'stavrosdenaxas.gif', 'kdavidwang.gif', 'vasugupta.gif']


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.player = Turtle()
        self.person = random.choice(THE_PEOPLE)
