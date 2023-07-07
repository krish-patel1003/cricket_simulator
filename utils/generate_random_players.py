import json
import random
import os
import sys

path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(path)

from models.players import Player

# Generate a json file with random player data
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
    player_data = {
        'name': name,
        'bowling': bowling,
        'batting': batting,
        'fielding': fielding,
        'running': running,
        'experience': experience,
        'speciality': player_object.speciality
    }
    players.append(player_data)


# Save the list of players to a JSON file
filename = 'players.json'
with open(filename, 'w') as file:
    json.dump(players, file, indent=4)

print("batsmen:", batsmen, "bowlers:", bowlers, "all-rounders:", all_rounders)
print(f"Player data saved to {filename} successfully.", )
