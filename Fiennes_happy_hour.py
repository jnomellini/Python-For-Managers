import random

bars = ["The Hamilton",
        "1020 Bar",
        "The Heights",
        "The Dead Poet"]

people = ["Mattan",
          "that person you forgot to text back",
          "Glenn Hubbard",
          "Samuel L. Jackson"
          ,"Ralph Fiennes"]

random_bar = random.choice(bars)
random_person1 = random.choice(people)
random_person2 = random.choice(people)

print(f"How about you go to {random_bar} with {random_person1} and {random_person2}?")
