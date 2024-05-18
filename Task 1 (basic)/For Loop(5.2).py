# 2. Imagine you are doing a workout routine, and you have to complete 100
# jumping jacks.

total_jumping_jacks = 100
jumping_jacks_per_set = 10
sets_completed = 0


while total_jumping_jacks > 0:
    print(f"Performing {jumping_jacks_per_set} jumping jacks...")


    total_jumping_jacks -= jumping_jacks_per_set

    # Increment the sets_completed
    sets_completed += 1

    if total_jumping_jacks == 0:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").lower()

    if tired in ["yes", "y"]:
        skip_remaining_sets = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip_remaining_sets in ["yes", "y"]:
            print(f"You completed a total of {sets_completed * jumping_jacks_per_set} jumping jacks.")
            break
    else:

        remaining_jumping_jacks = total_jumping_jacks

        print(f"{remaining_jumping_jacks} jumping jacks remaining.")
