"""
game_logic.py
Created: 01.04.26 14:33
Author: natalya
Project: Snowman-Meltdown

"""
import random
import sys
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown", "programming",
		 "computer", "keyboard", "algorithm", "developer"]
MAX_MISTAKES = len(STAGES) - 1  # Maximum number of mistakes allowed


def get_random_word():
	"""Selects a random word from the list."""
	return random.choice(WORDS)


def clear_screen():
	"""Clear the terminal screen for better readability."""
	# For Windows and Unix-like systems
	import os
	os.system('cls' if os.name == 'nt' else 'clear')


def display_game_state(mistakes, secret_word, guessed_letters):
	"""Display the current game state including snowman ASCII art and word progress."""
	print("\n" + "=" * 50)
	print("        SNOWMAN MELTDOWN")
	print("=" * 50)

	# Display the snowman stage for the current number of mistakes
	if mistakes <= MAX_MISTAKES:
		print(STAGES[mistakes])
	else:
		print(STAGES[MAX_MISTAKES])

	# Show mistake counter with visual indicator
	print(f"Mistakes: {mistakes}/{MAX_MISTAKES} ", end="")
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
	"""Check if all letters in the secret word have been guessed."""
	for letter in secret_word:
		if letter not in guessed_letters:
			return False
	return True


def get_valid_guess(guessed_letters):
	"""Get and validate a single alphabetical character guess."""
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
			print(f"⚠️  You already guessed '{guess.upper()}'. Try a different letter.\n")
			continue

		return guess


def play_again():
	"""Ask the user if they want to play again."""
	while True:
		answer = input("\n🎮 Would you like to play again? (y/n): ").lower().strip()
		if answer == 'y' or answer == 'yes':
			return True
		elif answer == 'n' or answer == 'no':
			return False
		else:
			print("Please enter 'y' for yes or 'n' for no.")


def display_welcome():
	"""Display welcome message and game instructions."""
	print("\n" + "=" * 50)
	print("        WELCOME TO SNOWMAN MELTDOWN!")
	print("=" * 50)
	print("\n📖 INSTRUCTIONS:")
	print("• Try to guess the secret word one letter at a time")
	print("• Each wrong guess makes the snowman melt more")
	print(f"• You have {MAX_MISTAKES} wrong guesses before the snowman melts completely")
	print("• Guess all letters correctly to save the snowman!")
	print("\n" + "=" * 50 + "\n")

	input("Press Enter to start the game...")
	clear_screen()


def play_game():
	"""Main game function to run Snowman Meltdown."""
	while True:
		# Clear screen for fresh game
		clear_screen()

		# Show welcome message for first game or replay
		if not hasattr(play_game, "first_game_done"):
			display_welcome()
			play_game.first_game_done = True
		else:
			print("\n" + "=" * 50)
			print("        NEW GAME!")
			print("=" * 50 + "\n")

		# Initialize game variables
		secret_word = get_random_word()
		guessed_letters = []
		mistakes = 0

		print(f"🌟 The secret word has {len(secret_word)} letters.")
		print(f"🌟 You have {MAX_MISTAKES} wrong guesses to save the snowman!\n")

		# Main game loop
		while True:
			# Display current game state
			display_game_state(mistakes, secret_word, guessed_letters)

			# Check win condition
			if is_word_guessed(secret_word, guessed_letters):
				print("🎉" * 10)
				print(f"🎉 CONGRATULATIONS! You saved the snowman! 🎉")
				print(f"🎉 The word was: {secret_word.upper()} 🎉")
				print("🎉" * 10)
				break

			# Check loss condition
			if mistakes >= MAX_MISTAKES:
				print("💀" * 10)
				print(f"💀 OH NO! The snowman has melted completely! 💀")
				print(f"💀 The word was: {secret_word.upper()} 💀")
				print("💀 Better luck next time! 💀")
				print("💀" * 10)
				break

			# Get valid guess
			guess = get_valid_guess(guessed_letters)

			# Add letter to guessed letters
			guessed_letters.append(guess)

			# Check if the guess is in the secret word
			if guess in secret_word:
				# Count how many times the letter appears
				count = secret_word.count(guess)
				print(f"✅ GOOD GUESS! '{guess.upper()}' appears {count} time(s) in the word! ✅\n")
				input("Press Enter to continue...")
				clear_screen()
			else:
				mistakes += 1
				print(f"❌ SORRY! '{guess.upper()}' is not in the word. ❌")
				print(f"💔 The snowman is melting! Mistakes: {mistakes}/{MAX_MISTAKES} 💔\n")
				input("Press Enter to continue...")
				clear_screen()

		# Ask if user wants to play again
		if not play_again():
			print("\n" + "=" * 50)
			print("        Thanks for playing Snowman Meltdown!")
			print("        Goodbye! 👋")
			print("=" * 50 + "\n")
			break
		else:
			# Reset for next game
			clear_screen()
			continue

# TODO:
# 1. TERM environment variable not set entfernen
# 2. Rate Versuche von Länge des Wortes abhängig machen
# 3. DocStrings einfügen
# 4. PEP8 prüfen
# 5. if __name__ == "__main__": in snowman.py auslagern



if __name__ == "__main__":
	try:
		play_game()
	except KeyboardInterrupt:
		print("\n\n👋 Game interrupted. Thanks for playing!")
		sys.exit(0)