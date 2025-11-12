"""
Level 3: State Logic

Goal:
- Decide whether a substance is SOLID, LIQUID, or GAS based on temperature.
- Use the freezing point and the actual boiling point (which may change with pressure).

Rules:
- If temperature <= freezing_point  -> "SOLID"
- Elif temperature >= actual_boiling_point -> "GAS"
- Else -> "LIQUID"

How to test:
- Run: python run_levels.py
- Or test just this level: python -m tests.test_level3
"""

from typing import Optional


def decide_state(temperature: float, freezing_point: float, actual_boiling_point: float) -> Optional[str]:
    """
    Return "SOLID", "LIQUID", or "GAS" based on temperature and reference points.
    """
    # ============================================
    # YOUR ANSWER GOES HERE - Write if/elif/else logic
    # ============================================
    # TODO: Implement the state decision using if/elif/else
    # 
    # HINT 1: Start with an if statement checking if temperature <= freezing_point
    #         If true, set result_state = "SOLID"
    #
    # HINT 2: Add an elif statement checking if temperature >= actual_boiling_point
    #         If true, set result_state = "GAS"
    #
    # HINT 3: Add an else statement for everything else (between freezing and boiling)
    #         Set result_state = "LIQUID"
    #
    # Example structure:
    #   if condition1:
    #       result_state = "SOLID"
    #   elif condition2:
    #       result_state = "GAS"
    #   else:
    #       result_state = "LIQUID"
    
    result_state = None
    # ⬇️ WRITE YOUR if/elif/else LOGIC BELOW THIS LINE ⬇️
    
    
    # ⬇️ WRITE YOUR CODE ABOVE THIS LINE ⬇️

    return result_state


