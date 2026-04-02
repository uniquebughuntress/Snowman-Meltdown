"""
snowman.py
Created: 26.03.26 12:58
Author: natalya
Project: Snowman-Meltdown

"""

"""Main entry point for the Snowman Meltdown game."""
import sys
from game_logic import play_game

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
        sys.exit(0)