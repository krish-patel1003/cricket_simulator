import random
from functools import reduce


class Umpire:

    def __init__(self):
        self.score = 0
        self.wickets = 0
        self.overs = 0

    def toss(self, pick):
        # Randomly select a team to bat first
        toss = random.randint(0, 1)
        return True if toss == pick else False

    def make_decision(self, batsman_on_strike, batsman_on_non_strike, bowling_team, ball_result):
        # Make decisions on caught, run out.
        umpires_decision = None

        if ball_result == "caught":
            fielder = random.choice(bowling_team.players)
            if fielder.fielding > 0.5:
                umpires_decision = "out"
            else:
                random_ball_result = random.choice(
                    batsman_on_strike.SCORE_TYPES)
                umpires_decision = random_ball_result

        if ball_result == "run out":

            batsman_on_danger_end = batsman_on_strike if random.randint(0, 1) == 0 else batsman_on_non_strike
            bowling_team_feilding_avg = reduce(
                lambda x, y: x + y, [player.fielding for player in bowling_team.players]) / len(bowling_team.players)
            
            if batsman_on_danger_end.running > bowling_team_feilding_avg:
                umpires_decision = "run out"
            
            else:
                if batsman_on_danger_end == batsman_on_strike:
                    random_ball_result = random.choice(["2 run"])
                    umpires_decision = random_ball_result
                else:
                    random_ball_result = random.choice(["1 run", "3 runs"])
                    umpires_decision = random_ball_result
                
        return umpires_decision
