import random
import os
import sys

path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(path)

from utils.play_ball_result import play_ball_result

class Player:

    BALL_RESULT_TYPES = [
        "out", "no ball", "wide", "dot", "1 run", "2 runs", "3 runs", "4 runs", "6 runs"]
    
    SCORE_TYPES = ["1 run", "2 runs", "3 runs", "4 runs", "6 runs"]
    
    OUT_TYPES = [ "caught", "bowled", "run out", "stumped", "lbw" ]

    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name
        self.bowling = bowling
        self.batting = batting  
        self.fielding = fielding
        self.running = running
        self.experience = experience
        self.speciality = None
        
    def __str__(self):
        return self.name
    
    def get_stats(self):
        return {
            'name': self.name,
            'bowling': self.bowling,
            'batting': self.batting,
            'fielding': self.fielding,
            'running': self.running,
            'experience': self.experience
        }
    
    def set_speciality(self):

        bowling = self.bowling
        batting = self.batting

        if bowling > 0.7 and batting < 0.5:
            self.speciality = 'bowler'
        elif batting > 0.7 and bowling < 0.5:
            self.speciality = 'batsman'
        elif batting > 0.5 and bowling > 0.5:
            self.speciality = 'all-rounder'
        else:
            if bowling > batting:
                self.speciality = 'bowler'
            else:   
                self.speciality = 'batsman'
        
        return self.speciality
        

    def play_ball(self, bowler):
        # Play a ball
        ball_result = play_ball_result(self, bowler, self.BALL_RESULT_TYPES)
        if ball_result == 'out':
            out_type = random.choice(self.OUT_TYPES)
            return out_type
        else:
            return ball_result
        
    

