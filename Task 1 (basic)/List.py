# Initial list of Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# Task 1: Calculate the number of members in the Justice League
print("Number of members in the Justice League:", len(justice_league))

# Task 2: Batman recruited Batgirl and Nightwing as new members. Add them to the list.
justice_league.extend(["Batgirl", "Nightwing"])
print("Justice League after recruiting Batgirl and Nightwing:", justice_league)

# Task 3: Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Justice League after making Wonder Woman the leader:", justice_league)

# Task 4: Choose "Green Lantern" and move them in between Aquaman and Flash.
chosen_hero = "Green Lantern"
justice_league.remove(chosen_hero)
justice_league.insert(justice_league.index("Aquaman") + 1, chosen_hero)
print("Justice League after separating Aquaman and Flash:", justice_league)

# Task 5: Replace the existing list with a new team assembled by Superman.
new_team = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league = new_team
print("Justice League after assembling a new team by Superman:", justice_league)

# Task 6: Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
justice_league.sort()
print("Justice League after sorting alphabetically (new leader predicted to be:", justice_league[0], "):", justice_league)
