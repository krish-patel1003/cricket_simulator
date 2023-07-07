import random

class Umpire:
    def __init__(self):
        self.score = 0
        self.wickets = 0
        self.overs = 0

    def toss(self, team, pick):
        # Randomly select a team to bat first
        toss = random.randint(0, 1)
        return True if toss == pick else False      

    def predict_outcome(self, bowler, batsman):
        # Predict the outcome of a ball based on the bowler and batsman stats
        pass

    def make_decision(self):
        # Make decisions on LBWs, catches, no-balls, wide-balls, etc.
        pass
