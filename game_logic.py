"""
game_logic.py
Created: 01.04.26 14:33
Author: natalya
Project: Snowman-Meltdown

"""

"""Game logic for Snowman Meltdown.

This module contains all the core game mechanics including word selection,
game state display, input validation, and the main game loop.
"""

import os
import random
from ascii_art import STAGES

# List of secret words
WORDS = [
	"python",
	"git",
	"github",
	"snowman",
	"meltdown",
	"programming",
	"computer",
	"keyboard",
	"algorithm",
	"developer"
]


def clear_screen():
	"""Clear the terminal screen.

	Uses the appropriate system command based on the operating system:
	'cls' for Windows, 'clear' for Unix-like systems.
	Suppresses error output to avoid TERM warnings in IDEs.
	"""
	try:
		if os.name == 'nt':  # Windows
			os.system('cls')
		else:  # Unix/Linux/Mac
			# Redirect output to suppress TERM warnings
			os.system('clear > /dev/null 2>&1')
	except Exception:
		# If clearing fails, just print newlines
		print("\n" * 100)


def calculate_max_mistakes(secret_word):
	"""Calculate the maximum number of mistakes allowed based on word length.

	The snowman gets more chances for longer words:
	- Short words (1-4 letters): 3 mistakes
	- Medium words (5-7 letters): 5 mistakes
	- Long words (8+ letters): 7 mistakes

	Args:
		secret_word (str): The word to calculate mistakes for.

	Returns:
		int: Maximum number of mistakes allowed.
	"""
	word_length = len(secret_word)
	if word_length <= 4:
		return 3
	elif word_length <= 7:
		return 5
	else:
		return 7


def get_random_word():
	"""Select a random word from the predefined word list.

	Returns:
		str: A randomly chosen word from the WORDS list.
	"""
	return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters, max_mistakes):
	"""Display the current game state.

	Shows the snowman ASCII art for the current number of mistakes,
	the word with revealed letters, and the list of guessed letters.

	Args:
		mistakes (int): Number of incorrect guesses made so far.
		secret_word (str): The word the player is trying to guess.
		guessed_letters (list): List of letters the player has guessed.
		max_mistakes (int): Maximum number of mistakes allowed.
	"""
	print("\n" + "=" * 50)
	print("        SNOWMAN MELTDOWN")
	print("=" * 50)

	# Calculate which stage to show (ensure we don't exceed available stages)
	stage_index = min(mistakes, len(STAGES) - 1)
	print(STAGES[stage_index])

	# Show mistake counter with visual indicator
	print(f"Mistakes: {mistakes}/{max_mistakes} ", end="")
	if mistakes > 0:
		print("💧" * mistakes, end="")
	print("\n")

	# Build a display version of the secret word with better formatting
	display_word = ""
	for letter in secret_word:
		if letter in guessed_letters:
			display_word += f" {letter.upper()} "
		else:
			display_word += " _ "

	print("Word:", display_word)
	print("-" * 50)

	# Show guessed letters in a nice format
	if guessed_letters:
		guessed_sorted = sorted(guessed_letters)
		print(f"Guessed letters: {', '.join(guessed_sorted).upper()}")
	else:
		print("Guessed letters: None yet")

	print("=" * 50 + "\n")


def is_word_guessed(secret_word, guessed_letters):
	"""Check if all letters in the secret word have been guessed.

	Args:
		secret_word (str): The word to check.
		guessed_letters (list): List of letters that have been guessed.

	Returns:
		bool: True if all letters in secret_word are in guessed_letters,
			  False otherwise.
	"""
	for letter in secret_word:
		if letter not in guessed_letters:
			return False
	return True


def get_valid_guess(guessed_letters):
	"""Get and validate a single alphabetical character guess.

	Continuously prompts the user until a valid guess is provided.
	Valid guesses are single alphabetical characters that haven't been
	guessed before.

	Args:
		guessed_letters (list): List of letters already guessed.

	Returns:
		str: A valid, lowercase letter that hasn't been guessed before.
	"""
	while True:
		guess = input("Guess a letter: ").lower().strip()

		# Check if input is empty
		if not guess:
			print("❌ Please enter a letter.\n")
			continue

		# Check if input is a single character
		if len(guess) != 1:
			print("❌ Please enter only ONE letter.\n")
			continue

		# Check if input is a letter
		if not guess.isalpha():
			print("❌ Please enter a letter (a-z).\n")
			continue

		# Check if letter was already guessed
		if guess in guessed_letters:
			print(f"⚠️  You already guessed '{guess.upper()}'. "
				  f"Try a different letter.\n")
			continue

		return guess


def play_again():
	"""Ask the user if they want to play another game.

	Returns:
		bool: True if the user wants to play again, False otherwise.
	"""
	while True:
		answer = input("\n🎮 Would you like to play again? (y/n): ").lower().strip()
		if answer in ('y', 'yes'):
			return True
		if answer in ('n', 'no'):
			return False
		print("Please enter 'y' for yes or 'n' for no.")


def display_welcome(max_mistakes_for_example=3):
	"""Display the welcome message and game instructions.

	Shows the game title, instructions, and waits for the user to press
	Enter before starting the game.

	Args:
		max_mistakes_for_example (int): Example mistake count for instructions.
	"""
	print("\n" + "=" * 50)
	print("        WELCOME TO SNOWMAN MELTDOWN!")
	print("=" * 50)
	print("\n📖 INSTRUCTIONS:")
	print("• Try to guess the secret word one letter at a time")
	print("• Each wrong guess makes the snowman melt more")
	print("• The number of allowed mistakes depends on word length:")
	print("  - Short words (1-4 letters): 3 mistakes")
	print("  - Medium words (5-7 letters): 5 mistakes")
	print("  - Long words (8+ letters): 7 mistakes")
	print("• Guess all letters correctly to save the snowman!")
	print("\n" + "=" * 50 + "\n")

	input("Press Enter to start the game...")
	clear_screen()


def play_game():
	"""Run the main Snowman Meltdown game.

	This function implements the complete game loop including:
	- Displaying welcome message on first run
	- Managing multiple game sessions
	- Handling player guesses and game state
	- Determining win/loss conditions
	- Offering replay option after each game
	"""
	first_game_done = False

	while True:
		# Clear screen for fresh game
		clear_screen()

		# Initialize game variables
		secret_word = get_random_word()
		guessed_letters = []
		mistakes = 0
		max_mistakes = calculate_max_mistakes(secret_word)

		# Show welcome message for first game or replay
		if not first_game_done:
			display_welcome(max_mistakes)
			first_game_done = True
		else:
			print("\n" + "=" * 50)
			print("        NEW GAME!")
			print("=" * 50 + "\n")

		print(f"🌟 The secret word has {len(secret_word)} letters.")
		print(f"🌟 You have {max_mistakes} wrong guesses to save the snowman!\n")

		# Main game loop
		while True:
			# Display current game state
			display_game_state(mistakes, secret_word, guessed_letters, max_mistakes)

			# Check win condition
			if is_word_guessed(secret_word, guessed_letters):
				print(f"🎉 CONGRATULATIONS! You saved the snowman! 🎉")
				print(f"🎉 The word was: {secret_word.upper()} 🎉")
				break

			# Check loss condition
			if mistakes >= max_mistakes:
				print(f"💀 OH NO! The snowman has melted completely! 💀")
				print(f"The word was: {secret_word.upper()}")
				print("Better luck next time!")
				break

			# Get valid guess
			guess = get_valid_guess(guessed_letters)

			# Add letter to guessed letters
			guessed_letters.append(guess)

			# Check if the guess is in the secret word
			if guess in secret_word:
				# Count how many times the letter appears
				count = secret_word.count(guess)
				print(f"✅ GOOD GUESS! '{guess.upper()}' appears {count} "
					  f"time(s) in the word! ✅\n")
#				input("Press Enter to continue...")
				clear_screen()
			else:
				mistakes += 1
				print(f"❌ SORRY! '{guess.upper()}' is not in the word. ❌")
				print(f"💔 The snowman is melting! Mistakes: "
					  f"{mistakes}/{max_mistakes} 💔\n")
#				input("Press Enter to continue...")
				clear_screen()

		# Ask if user wants to play again
		if not play_again():
			print("\n" + "=" * 50)
			print("        Thanks for playing Snowman Meltdown!")
			print("        Goodbye! 👋")
			print("=" * 50 + "\n")
			break
