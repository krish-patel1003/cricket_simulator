

class Player:

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
        

    def play_ball(self):
        pass
    
