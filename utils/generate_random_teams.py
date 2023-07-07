import json
import models.players as players
import models.teams as teams


def create_players_from_json():
    file_path = '../players.json'
    players = []
    bowler, batsman, all_rounder = [], [], []
    with open(file_path, 'r') as file:
        player_data = json.load(file)

    for player_info in player_data:
        player = players.Player(player_info['name'], player_info['bowling'], player_info['batting'],
                        player_info['fielding'], player_info['running'], player_info['experience'])
        players.append(player)
        player.set_speciality()
        if player.speciality == 'bowler':
            bowler.append(player)
        elif player.speciality == 'batsman':
            batsman.append(player)
        else:
            all_rounder.append(player)




    return players, bowler, batsman, all_rounder

def create_teams(players, teamA_name, teamB_name):

    # Create team objects
    teamA = teams.Team(teamA_name)
    teamB = teams.Team(teamB_name)


    # Logic for Auto-balancing teams
    # players, bowlers, batsmen, all_rounders = create_players_from_json()

    # bowlers = sorted(bowlers, key=lambda x: x.bowling, reverse=True)
    # batsmen = sorted(batsmen, key=lambda x: x.batting, reverse=True)
    # all_rounders = sorted(all_rounders, key=lambda x: x.batting, reverse=True)

    # players_per_speciality = min(len(bowlers), len(batsmen))

    # for _ in range(players_per_speciality):

    #     while not bowlers.is_empty():
    #         teamA.add_player(bowlers.pop())
    #         teamB.add_player(bowlers.pop())
        

    # Add players to the teams
    for i in range(0, len(players), 2):
        teamA.add_player(players[i])
        teamB.add_player(players[i+1])
        