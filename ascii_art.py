"""
ascii_art.py
Created: 01.04.26 14:33
Author: natalya
Project: Snowman-Meltdown

"""
"""Snowman ASCII art stages for the Snowman Meltdown game.

This module contains the visual representation of the snowman at different
melting stages. Each stage shows progressive melting from a full snowman
to just a puddle.
"""

# Snowman ASCII Art stages - Enhanced with more stages for smoother melting
STAGES = [
    # Stage 0: Full snowman
    """
       ___
      /___\\
      (o o)
      ( : )
      ( : )
    """,
    # Stage 1: Snowman starts melting - bottom starts to droop
    """
       ___
      /___\\
      (o o)
      ( : )
      ( . )
    """,
    # Stage 2: Bottom part partially melted
    """
       ___
      /___\\
      (o o)
      ( : )
    """,
    # Stage 3: Bottom part completely melted, middle starts drooping
    """
       ___
      /___\\
      (o o)
      ( . )
    """,
    # Stage 4: Only the head remains
    """
       ___
      /___\\
      (o o)
    """,
    # Stage 5: Head starts melting
    """
       ___
      /___\\
      (o .)
    """,
    # Stage 6: Head partially melted
    """
       ___
      /___\\
      ( . )
    """,
    # Stage 7: Snowman completely melted - only puddle remains
    """
       ___
      /___\\
      (   )
    """,
    # Stage 8: Just a puddle
    """
        ___
       /___\\
    """
]