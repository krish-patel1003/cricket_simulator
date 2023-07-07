import json
import random
import os
import sys

path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(path)

from models.players import Player

# Generate a json file with random player data
def generate_random_players():
    
    players = []
    batsmen = 0
    bowlers = 0
    all_rounders = 0
    for i in range(30):
        name = f"Player {i+1}"
        bowling = round(random.uniform(0.1, 1.0), 2)
        batting = round(random.uniform(0.1, 1.0), 2)
        fielding = round(random.uniform(0.1, 1.0), 2)
        running = round(random.uniform(0.1, 1.0), 2)
        experience = round(random.uniform(0.1, 1.0), 2)
        player_object = Player(name, bowling, batting, fielding, running, experience)
        speciality = player_object.set_speciality()
        if speciality == 'batsman':
            batsmen += 1
        elif speciality == 'bowler':
            bowlers += 1
        else:
            all_rounders += 1

        players.append(player_object)

    print(
        "batsmen:", batsmen, "bowlers:", bowlers, "all-rounders:", all_rounders)
    return players


if __name__ == "__main__":
    players = generate_random_players()
    players_json = [player.__dict__ for player in players]
    with open('players.json', 'w') as file:
        json.dump(players_json, file, indent=4)
    