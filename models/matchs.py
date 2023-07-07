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
        self.match_info = {}
        self.umpire = umpire.Umpire()

    def set_innings(self, batting_team, bowling_team):
        # Select the batting and bowling teams for the first innings
        self.current_batting_team = batting_team
        self.current_bowling_team = bowling_team

    def change_innings(self):
        # Swap the batting and bowling teams for the next innings
        self.current_innings += 1
        self.current_batting_team, self.current_bowling_team = self.current_bowling_team, self.current_batting_team
        self.play_innings()

    def end_match(self):
        # End the match and display the final result
        print("Match ended.")
        # You can display the final score, wickets, overs, etc.

    def play_innings(self):
        # Simulate the innings
        print(
            f"Innings {self.current_innings} - {self.current_batting_team.name} batting")
        
        # playing innnings logic
        # while True:
        #     pass
        #     if self.is_innings_ended():
        #         break

        # if self.current_innings < 2:
        #     self.change_innings()
        # else:
        #     self.end_match()

    def is_innings_ended(self):
        # Check if the innings has ended based on the match situation
        pass

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
        pass