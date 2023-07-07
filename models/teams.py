

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.captain = None
        self.home_ground = None
    
    def set_home_ground(self, ground):
        self.home_ground = ground

    def add_player(self, player):
        # Add a player to the team
        self.players.append(player)

    def select_captain(self):
        # Select a captain from the team's players
        pass

    def send_next_player(self):
        # Select the next player to go to the field
        pass

    def choose_bowler(self):
        # Choose a bowler for the next over
        pass

    def decide_batting_order(self):
        # Decide the batting order
        pass