import os
import sys
import json
import random

path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(path)

from models import fields

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
    home_advantage = random.choice([0, 1])
    field = fields.Field(field_name, field_size, fan_ratio, pitch_conditions, home_advantage)

    return field


if __name__ == "__main__":
    field_name = "Random Field"
    field = generate_a_random_field(field_name)
    print(field.__dict__)
    with open('field.json', 'w') as file:
        json.dump(field.__dict__, file, indent=4)
