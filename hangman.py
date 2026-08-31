import random
 
words = ["apple", "bread", "chair", "grape", "house"]
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")
print("Guess the five-letter word one letter at a time.")

while wrong_guesses < max_wrong_guesses:
	display_word = ""

	for letter in word:
		if letter in guessed_letters:
			display_word += letter + " "
		else:
			display_word += "_ "

	print("\nWord:", display_word)
	print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

	if "_" not in display_word:
		print("You win! The word was:", word)
		break

	guess = input("Guess a letter: ").lower()

	if len(guess) != 1 or not guess.isalpha():
		print("Please enter one letter.")
	elif guess in guessed_letters:
		print("You already guessed that letter.")
	else:
		guessed_letters.append(guess)

		if guess in word:
			print("Good guess!")
		else:
			wrong_guesses += 1
			print("That letter is not in the word.")
else:
	print("\nYou lose! The word was:", word)
