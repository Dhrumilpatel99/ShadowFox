# 1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20
# times).
# Count and print the following statistics:
# How many times you rolled a 6
# How many times you rolled a 1
# How many times you rolled two 6s in a row


import random

# Initialize variables to count statistics
num_rolls = 20
num_six = 0
num_one = 0
num_two_sixes_in_a_row = 0
previous_roll = None


for _ in range(num_rolls):
    roll = random.randint(1, 6)
    # Simulate rolling a die (generate a random number between 1 and 6)

    # Count the number of times 6 is rolled
    if roll == 6:
        num_six += 1

    # Count the number of times 1 is rolled
    if roll == 1:
        num_one += 1

    # Count the number of times two 6s in a row are rolled
    if roll == 6 and previous_roll == 6:
        num_two_sixes_in_a_row += 1

    # Update previous roll for the next iteration
    previous_roll = roll

# Print the statistics
print("Number of times rolled a 6:", num_six)
print("Number of times rolled a 1:", num_one)
print("Number of times rolled two 6s in a row:", num_two_sixes_in_a_row)
