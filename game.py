# import the local files and other dependencies
from game_data import data
import random

#  keep track of score
score = 0


def choose_celeb():
    rand_index = random.randint(0, (len(data) - 1))
    celeb = data[rand_index]
    data.remove(celeb)
    return celeb


#  return the celeb in a ledgible fashion
def comprehend_celeb(who):
    name = who['name']
    description = who['description']
    country = who['country']
    return f"{name}, a {description}, from {country}."


#  user takes a guess
def highlow():
    userguess = input("Higher or lower? Type 'h' or 'l'. \n")
    if userguess == 'h':
        return True
    else:
        return False


#  compare the two items
def compare_followers(a, b):
    a_followers = a['follower_count']
    b_followers = b['follower_count']
    if a_followers < b_followers:
        return True
    else:
        return False


#  deal with correct scenario/make gameplay loop
gameplay = True
celeba = choose_celeb()
celebb = choose_celeb()

while gameplay:
    print(f"Compare A : {comprehend_celeb(celeba)}")
    print("vs")
    print(f"With B : {comprehend_celeb(celebb)}")
    if compare_followers(celeba, celebb) == highlow():
        print('correct')
        celeba = celebb
        celebb = choose_celeb()
        score += 1
    else:
        print(f"incorrect, game over. Your score was {score}")
        gameplay = False
