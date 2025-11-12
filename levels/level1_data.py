"""
Level 1: Liquid Data

Goal:
- Create a dictionary of liquids with their names and temperature points.
- Keys should be lowercase simple ids like "water" and "ethanol".
- Each value is a dictionary with keys: name, freezing_point, boiling_point.

How to test:
- Run: python run_levels.py
- Or test just this level: python -m tests.test_level1
"""

from typing import Dict, Any


def get_default_liquids() -> Dict[str, Dict[str, Any]]:
    """
    Return default liquid data.

    Each entry should look like:
    "water": {"name": "Water (H2O)", "freezing_point": 0.0, "boiling_point": 100.0}
    """
    return {
        # ============================================
        # YOUR ANSWER GOES HERE - Fill in the dictionary below
        # ============================================
        
        # TODO: Add water data here (freezing: 0.0, boiling: 100.0)
        # Example: "water": {"name": "Water (H2O)", "freezing_point": 0.0, "boiling_point": 100.0}
        # ⬇️ WRITE YOUR CODE BELOW THIS LINE ⬇️
        
        
        # TODO: Add ethanol data here (freezing: -114.1, boiling: 78.4)
        # Example: "ethanol": {"name": "Ethanol (C₂H₅OH)", "freezing_point": -114.1, "boiling_point": 78.4}
        # ⬇️ WRITE YOUR CODE BELOW THIS LINE ⬇️
        
        
        # TODO: Add at least one more liquid of your choice
        # Example: "milk": {"name": "Milk", "freezing_point": -0.5, "boiling_point": 100.2}
        # ⬇️ WRITE YOUR CODE BELOW THIS LINE ⬇️
        
        
    }


