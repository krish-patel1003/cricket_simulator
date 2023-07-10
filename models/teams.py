

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.captain = None
        self.home_advantage = "home"
    
    def set_home_advantage(self, home_advantage):
        self.home_ground = home_advantage

    def add_player(self, player):
        # Add a player to the team
        self.players.append(player)
    
    def print_team(self):
        # Print the team
        for player in self.players:
            print(player.__dict__)
        

    def select_captain(self):
        # Select a captain from the team's players
        players = sorted(self.players, key=lambda x: x.experience, reverse=True)
        max_skill_avg = 0
        for player in players:
            player_skill_avg = (player.batting + player.bowling + player.fielding + player.running)/4
            if player_skill_avg > max_skill_avg:
                self.captain = player
                max_skill_avg = player_skill_avg
        return self.captain 

    def next_batsman(self, wickets):
        # Select the next batsmen to go to the field
        batsmen = sorted(self.players, key=lambda x: x.batting,reverse=True)[1+wickets:]
        
        return batsmen[0]


    def select_bowler(self, over):
        # Choose a bowler for the next over
        bowlers = sorted(self.players, key=lambda x: x.bowling, reverse=True)
        index = over%len(bowlers)
        return bowlers[index]


    def decide_batting_order(self):
        # Decide the batting order
        batting_order = sorted(self.players, key=lambda x: x.batting, reverse=True)
        return batting_order
