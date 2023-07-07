import os
import sys
import json
import random

path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(path)

pitch_types = [
    "flat",
    "green",
    "dusty",
    "slow and low",
    "hard and bouncy",
]

def generate_a_random_field(field_name):
    # Generate a random field
    field_size = random.randint(60, 90)
    fan_ratio = "1:1"
    pitch_conditions = random.choice(pitch_types)
    home_advantage = None
    field_data = {
        'field_name': field_name,
        'field_size': field_size,
        'fan_ratio': fan_ratio,
        'pitch_conditions': pitch_conditions,
        'home_advantage': home_advantage
    }
    return field_data


def dump_field_in_json(field):
    # Save the field data to a JSON file
    filename = 'field.json'
    with open(filename, 'w') as file:
        json.dump(field, file, indent=4)
    
    print(f"Field data saved to {filename} successfully.", )


if __name__ == "__main__":
    field_name = "Random Field"
    field = generate_a_random_field(field_name)
