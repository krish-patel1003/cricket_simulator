import os
import sys



import models.umpire as umpire


class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.current_innings = 1
        self.current_batting_team = None
        self.current_bowling_team = None
        self.overs = None
        self.match_info = {}
        self.umpire = umpire.Umpire()
    
    def set_overs(self, overs):
        # Set the number of overs for the match
        self.overs = overs
        return self.overs

    def set_innings(self, batting_team, bowling_team):
        # Select the batting and bowling teams for the first innings
        self.current_batting_team = batting_team
        self.current_bowling_team = bowling_team

    def change_innings(self):
        # Swap the batting and bowling teams for the next innings
        self.current_innings += 1
        self.current_batting_team, self.current_bowling_team = self.current_bowling_team, self.current_batting_team
        if self.current_innings > 2:
            self.end_match()
            return
        self.play_innings()

    def end_match(self):
        # End the match and display the final result
        print("Match ended.")
        team1_score = self.match_info[f"{self.team1.name}_score"]
        team2_score = self.match_info[f"{self.team2.name}_score"]
        if team1_score > team2_score:
            self.update_match_info("winner", f"{self.team1.name}")
        else:
            self.update_match_info("winner", f"{self.team2.name}")
        
        self.get_match_summary()
        # You can display the final score, wickets, overs, etc.

    def play_innings(self):
        # Simulate the innings
        print(
            f"Innings {self.current_innings} - {self.current_batting_team.name} batting")
        
        score = 0
        wickets = 0
        extras = 0
        
        self.update_match_info("innings", self.current_innings)
        self.update_match_info("batting_team", self.current_batting_team.name)
        self.update_match_info("bowling_team", self.current_bowling_team.name)
        self.update_match_info(f"{self.current_batting_team.name}_score", 0)    
        self.update_match_info(f"{self.current_batting_team.name}_wickets", 0)
        self.update_match_info(f"{self.current_batting_team.name}_extras", 0)
        self.update_match_info(f"Innings {self.current_innings}", {})


        
        batsman_on_strike, batsman_on_non_strike = self.current_batting_team.decide_batting_order()[0:2]
        
        for over in range(self.overs):
            bowler = self.current_bowling_team.select_bowler(over)

            self.add_over_in_innings(over+1)

            if over != 0:
                batsman_on_strike, batsman_on_non_strike = batsman_on_non_strike, batsman_on_strike

            for ball in range(1, 7):
                print(f"Over {over}.{ball}")
                print(f"Bowler: {bowler.name}")
                print(
                    f"Batsmen: {batsman_on_strike.name} and {batsman_on_non_strike.name}")
                ball_result = batsman_on_strike.play_ball(bowler)

                if ball_result == "wide" or ball_result == "no ball":
                    ball_again = True
                    while ball_again:
                        self.update_over_info(over+1, "ball_again", ball_result)
                        print("Ball again")
                        score += 1
                        extras += 1
                        ball_again_result = batsman_on_strike.play_ball(bowler)

                        if ball_result == "no ball" and ball_again_result in ["caught", "bowled", "lbw", "stumped"]:
                            ball_result = "dot"
                            ball_again =  False
                            break
                        
                        print(ball_result)
                        if ball_again_result != "wide" and ball_again_result != "no ball":
                            ball_result = ball_again_result
                            ball_again = False

                if ball_result in ["1 run", "3 runs"]:
                    batsman_on_non_strike, batsman_on_strike = batsman_on_strike, batsman_on_non_strike

                if ball_result in batsman_on_strike.OUT_TYPES:
                    print(f"{batsman_on_strike.name} is out!")
                    wickets += 1
                    self.update_match_info(
                        f"{self.current_batting_team.name}_wickets", wickets)
                    
                    if wickets == 10:
                        print("All out!")
                        break
                    batsman_on_strike = self.current_batting_team.next_batsman(wickets)
                    print(f"New batsman: {batsman_on_strike.name}")
                
                if ball_result in batsman_on_strike.SCORE_TYPES:
                    score += int(ball_result.split(" ")[0])

                print("ball_result: ", ball_result)
                self.update_over_info(over+1, ball, ball_result)
                self.update_match_info(
                    f"{self.current_batting_team.name}_score", score)
                self.update_match_info(f"{self.current_batting_team.name}_extras", extras)

            print(self.get_match_info())   

        self.change_innings()
        return self.match_info
        
        

    def get_match_summary(self):
        # Display the match summary
        print("Match Summary")
        print("-------------")
        print(f"Venue: {self.field.field_name}")
        print(f"Team 1: {self.team1.name}")
        print(f"Team 2: {self.team2.name}")
        print(f"Winner: {self.match_info['winner']}")

    def get_match_info(self):
        # Return the match info
        return self.match_info
    
    def update_match_info(self, key, value):
        # Update the match info
        self.match_info[key] = value
        return self.match_info
    
    def update_over_info(self, over, ball, ball_result):
        # Update the over info
        over = self.match_info[f"Innings {self.current_innings}"]["over - "+str(over)]
        over.setdefault(ball, ball_result)
        return self.match_info

    def add_over_in_innings(self, over):
        # Add the over in innings
        innings = self.match_info[f"Innings {self.current_innings}"]
        innings.setdefault("over - "+str(over), {})

    def start_match(self):
        # Start the match
        print("Match Started!")
        self.play_innings()
    
    def get_match_info(self):
        # Return the match info
        return self.match_info