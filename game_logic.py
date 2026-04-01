"""
game_logic.py
Created: 01.04.26 14:33
Author: natalya
Project: Snowman-Meltdown

"""
import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1  # Maximum number of mistakes allowed (3)


def get_random_word():
	"""Selects a random word from the list."""
	return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
	"""Display the current game state including snowman ASCII art and word progress."""
	# Display the snowman stage for the current number of mistakes
	# Ensure we don't try to access an index that doesn't exist
	if mistakes <= MAX_MISTAKES:
		print(STAGES[mistakes])
	else:
		print(STAGES[MAX_MISTAKES])  # Show the final melted stage

	# Build a display version of the secret word
	display_word = ""
	for letter in secret_word:
		if letter in guessed_letters:
			display_word += letter + " "
		else:
			display_word += "_ "
	print("Word: ", display_word)

	# Show guessed letters so far
	if guessed_letters:
		print("Guessed letters:", ", ".join(sorted(guessed_letters)))
	print("\n")


def is_word_guessed(secret_word, guessed_letters):
	"""Check if all letters in the secret word have been guessed."""
	for letter in secret_word:
		if letter not in guessed_letters:
			return False
	return True


def play_game():
	"""Main game function to run Snowman Meltdown."""
	secret_word = get_random_word()
	guessed_letters = []
	mistakes = 0

	print("Welcome to Snowman Meltdown!")
	print("Try to save the snowman by guessing the word before he melts!")
	print(f"The word has {len(secret_word)} letters.")
	print()

	# Main game loop - continue while game is still active
	while True:
		# Display current game state
		display_game_state(mistakes, secret_word, guessed_letters)

		# Check win condition
		if is_word_guessed(secret_word, guessed_letters):
			print(f"Congratulations! You saved the snowman!")
			print(f"The word was: {secret_word}")
			break

		# Check loss condition
		if mistakes >= MAX_MISTAKES:
			print(f"Oh no! The snowman has melted completely!")
			print(f"The word was: {secret_word}")
			print("Better luck next time!")
			break

		# Get player's guess
		guess = input("Guess a letter: ").lower().strip()

		# Validate input
		if len(guess) != 1 or not guess.isalpha():
			print("Please enter a single letter.\n")
			continue

		# Check if letter was already guessed
		if guess in guessed_letters:
			print(f"You already guessed '{guess}'. Try a different letter.\n")
			continue

		# Add letter to guessed letters
		guessed_letters.append(guess)

		# Check if the guess is in the secret word
		if guess in secret_word:
			print(f"Good guess! '{guess}' is in the word.\n")
		else:
			print(f"Sorry, '{guess}' is not in the word.")
			mistakes += 1
			print(f"Mistakes: {mistakes}/{MAX_MISTAKES}\n")


