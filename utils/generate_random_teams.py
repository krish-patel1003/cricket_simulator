import json
import models.players as players
import models.teams as teams


def create_teams(players, teamA_name, teamB_name):

    # Create team objects
    teamA = teams.Team(teamA_name)
    teamB = teams.Team(teamB_name)

    # Add players to the teams
    for i in range(0, len(players), 2):
        teamA.add_player(players[i])
        teamB.add_player(players[i+1])

    return teamA, teamB
        