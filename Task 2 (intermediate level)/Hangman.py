import random


name = input("What is your name? ")

# enter the name first

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks', 'shadowfox']



word = random.choice(words)


print("Guess the characters")

guesses = ''


turns = 12


while turns > 0:


	failed = 0


	for char in word:

		# comparing that character with
		# the character in guesses
		if char in guesses:
			print(char, end=" ")

		else:
			print("_")

			# for every failure 1 will be
			# incremented in failure
			failed += 1

	if failed == 0:
		# user will win the game if failure is 0
		# and 'You Win' will be given as output
		print("You Win")

		print("The word is: ", word)
		break


	print()
	guess = input("guess a character:")

	# every input character will be stored in guesses
	guesses += guess


	if guess not in word:

		turns -= 1



		print("Wrong")



		print("You have", + turns, 'more guesses')

		if turns == 0:
			print("You Loose")

# to guess the answer type the shadowfox
# and type a another one one will be the correct and another one will be the wrong