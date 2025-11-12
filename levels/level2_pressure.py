"""
Level 2: Pressure Effect

Goal:
- Write a function to calculate how pressure changes the boiling point.
- Rule: For each +1.0 atm above normal, boiling point goes up by 10°C.
        For each -1.0 atm, it goes down by 10°C.
        Normal pressure is 1.0 atm.

Formula:
adjusted_boiling = base_boiling_point + (pressure - 1.0) * 10.0

How to test:
- Run: python run_levels.py
- Or test just this level: python -m tests.test_level2
"""

from typing import Optional


def calculate_pressure_effect(base_boiling_point: float, pressure: float) -> Optional[float]:
    """
    Return the boiling point adjusted for the given pressure.
    """
    # ============================================
    # YOUR ANSWER GOES HERE - Calculate the adjusted boiling point
    # ============================================
    # TODO: Calculate adjusted boiling point
    # Hint: pressure_difference = pressure - 1.0
    # Hint: adjusted = base_boiling_point + (pressure_difference * 10.0)
    # 
    # ⬇️ REPLACE THE NEXT LINE WITH YOUR CALCULATION ⬇️
    adjusted_boiling_point = None
    # ⬇️ WRITE YOUR CODE ABOVE THIS LINE ⬇️

    return adjusted_boiling_point


