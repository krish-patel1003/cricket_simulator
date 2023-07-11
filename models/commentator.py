

class Commentator:
    def __init__(self, name, match):
        self.name = name
        self.match = match

    def toss_commentary(self, match):
        # Provide commentary for each ball and over based on the match stats
        toss = match.match_info['toss']
        print(f"Commentator({self.name}): ", toss)
    
    def over_commentary(self, match, bowler):
        # Provide commentary for each ball and over based on the match stats
        pass
    
    def commentary(self, commentary):
        # Provide commentary for each ball and over based on the match stats
        print(f"Commentator({self.name}): ", commentary)
        

        
