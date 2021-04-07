import random

sports = ["Football",
        "Basketball",
        "Golf",
        "Waterpolo"]

equipment = ["Bowling Ball",
          "Hockey Puck",
          "Frisbee",
          "Cue Ball"]

random_sports = random.choice(sports)
random_equipment = random.choice(equipment)

print(f"What if you played {random_sports} with a {random_equipment}!?")
