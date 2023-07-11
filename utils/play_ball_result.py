import random
import os
import sys
import math

path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(path)

from models import players


def play_ball_result(batsman, bowler, ball_result_types):

    skill_difference = abs(batsman.batting - bowler.bowling)
    random_result = round(random.uniform(0.0, 1.0), 2)

    result_probability = skill_difference*random_result

    index = int(result_probability*(len(ball_result_types) * 10)) % len(ball_result_types)

    if ball_result_types[index] in batsman.SCORE_TYPES[:3]:
        index = int(result_probability*(batsman.running)*(300)) % 3
        return batsman.SCORE_TYPES[index]

    return ball_result_types[index]


if __name__ == "__main__":
    bowler = players.Player("Bowler", 0.66, 0.22, 0.82, 0.37, 0.55)
    batsman = players.Player("Batsman", 0.47, 1.0, 1.0, 0.23, 0.51)
    ball_result_types = ["out", "wide", "no ball", "dot", "1 run", "2 runs", "3 runs", "4 runs", "6 runs"]
    play_ball_result(batsman, bowler, ball_result_types)







