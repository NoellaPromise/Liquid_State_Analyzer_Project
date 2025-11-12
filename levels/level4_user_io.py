"""
Level 4: User Input Helpers

Goal:
- Write small helper functions that validate user input.
- These helpers are EASY to test because they don't call input() directly.

Functions to write:
- parse_choice(input_str, max_choice) -> int | None
  - Convert to int and ensure it's in [1, max_choice]
- parse_float(input_str) -> float | None
  - Convert to float if possible
- get_pressure_with_default(input_str) -> float | None
  - If input_str is empty, return 1.0
  - Else parse as float and ensure > 0

How to test:
- Run: python run_levels.py
- Or test just this level: python -m tests.test_level4
"""

from typing import Optional


def parse_choice(input_str: str, max_choice: int) -> Optional[int]:
    # ============================================
    # YOUR ANSWER GOES HERE - Write parse_choice function
    # ============================================
    # TODO: Convert input_str to an integer and validate it's in range [1, max_choice]
    #
    # HINT 1: Use try/except to handle conversion errors
    #         Example: try: number = int(input_str) except ValueError: return None
    #
    # HINT 2: After converting, check if 1 <= number <= max_choice
    #         If valid, return the number; otherwise return None
    #
    # Example structure:
    #   try:
    #       number = int(input_str)
    #       if 1 <= number <= max_choice:
    #           return number
    #       else:
    #           return None
    #   except ValueError:
    #       return None
    
    # ⬇️ REPLACE THE NEXT LINE WITH YOUR CODE ⬇️
    return None
    # ⬇️ WRITE YOUR CODE ABOVE THIS LINE ⬇️


def parse_float(input_str: str) -> Optional[float]:
    # ============================================
    # YOUR ANSWER GOES HERE - Write parse_float function
    # ============================================
    # TODO: Convert input_str to a float number
    #
    # HINT 1: Use try/except to handle conversion errors
    #         Example: try: number = float(input_str) except ValueError: return None
    #
    # HINT 2: If conversion succeeds, return the float number
    #         If it fails (raises ValueError), return None
    #
    # Example structure:
    #   try:
    #       return float(input_str)
    #   except ValueError:
    #       return None
    
    # ⬇️ REPLACE THE NEXT LINE WITH YOUR CODE ⬇️
    return None
    # ⬇️ WRITE YOUR CODE ABOVE THIS LINE ⬇️


def get_pressure_with_default(input_str: str) -> Optional[float]:
    # ============================================
    # YOUR ANSWER GOES HERE - Write get_pressure_with_default function
    # ============================================
    # TODO: Handle pressure input with a default value of 1.0
    #
    # HINT 1: Check if input_str is empty or only spaces using .strip()
    #         Example: if input_str.strip() == "": return 1.0
    #
    # HINT 2: If not empty, try to parse it as float (use parse_float or try/except)
    #
    # HINT 3: Check if the parsed number is > 0
    #         If yes, return it; if no, return None
    #
    # Example structure:
    #   if input_str.strip() == "":
    #       return 1.0
    #   else:
    #       number = parse_float(input_str)  # or use try/except
    #       if number is not None and number > 0:
    #           return number
    #       else:
    #           return None
    
    # ⬇️ REPLACE THE NEXT LINE WITH YOUR CODE ⬇️
    return None
    # ⬇️ WRITE YOUR CODE ABOVE THIS LINE ⬇️


