from utils import generate_a_random_field, generate_random_players, generate_random_teams
from models import teams, fields, matchs, players, umpire
import os
import sys
import json
import random

path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(path)


def prepare_teams(teamA_name, teamB_name, field):

    # Generate random players
    players = generate_random_players.generate_random_players()
    # print(players)

    # Create teams
    teamA, teamB = generate_random_teams.create_teams(
        players, teamA_name, teamB_name)

    if field.home_advantage == 1:
        teamA.set_home_advantage("away")
    else:
        teamB.set_home_advantage("away")

    return teamA, teamB


def prepare_innings(team_to_toss, other_team, match):

    bat_or_bowl = int(
        input(f"{team_to_toss.name} Choose bat(0) or bowl(1): "))
    if bat_or_bowl == 0:
        print(f"{team_to_toss.name} chose to bat first!")
        match.set_innings(team_to_toss, other_team)
    else:
        print(f"{team_to_toss.name} chose to bowl first!")
        match.set_innings(other_team, team_to_toss)




def prepare_match(teamA, teamB, field):

    # Create a match
    match = matchs.Match(teamA, teamB, field)
    team_to_toss = random.choice([0, 1])

    # Toss
    if team_to_toss == 0:
        team_to_toss = teamA
        other_team = teamB
    else:
        team_to_toss = teamB
        other_team = teamA
    

    toss_side_pick = int(input(f"{team_to_toss.name} Choose heads(0) or tails(1): "))
    toss_result = match.umpire.toss(toss_side_pick)

    if toss_result:
        print(f"{team_to_toss.name} won the toss!")
        prepare_innings(team_to_toss, other_team, match)

    else:
        print(f"{other_team.name} won the toss!")
        prepare_innings(other_team, team_to_toss, match)
       
    return match


def main():

    print("Let's prepare the match!")

    # Generate a random field
    field_name = input("Enter the field name: ")
    field = generate_a_random_field.generate_a_random_field(field_name)

    print("Field Details: ", field.__dict__)

    # Prepare Teams
    teamA_name = input("Enter Team A name: ")
    teamB_name = input("Enter Team B name: ")
    teamA, teamB = prepare_teams(teamA_name, teamB_name, field)

    print("Team Details: ")
    print(f"{teamA.name}: ")
    teamA.print_team()
    print(f"{teamB.name}: ")
    teamB.print_team()


    
    # Prepare the match and toss
    match = prepare_match(teamA, teamB, field)

    # Start the match
    match.start_match()




if __name__ == '__main__':
    main()




