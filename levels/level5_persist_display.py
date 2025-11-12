"""
Level 5: Save and Display

Goal:
- Save analysis results to a JSON file.
- Create a nicely formatted text block for the results.

Functions to write:
- save_analysis_result(results, filename="analysis_results.json") -> bool
  - If file exists, load the list, append results, and save back.
  - If it doesn't exist, create a new list with this one result.
  - Return True if saved successfully, False otherwise.
- format_results_text(results) -> str
  - Return a multi-line string with:
      Liquid name, Temperature, Pressure, STATE, and reference points.

How to test:
- Run: python run_levels.py
- Or test just this level: python -m tests.test_level5
"""

from typing import Dict, Any
import json
import os


def save_analysis_result(results: Dict[str, Any], filename: str = "data/analysis_results.json") -> bool:
    # ============================================
    # YOUR ANSWER GOES HERE - Write save_analysis_result function
    # ============================================
    # TODO: Save analysis results to a JSON file (append to existing list or create new)
    #
    # HINT 1: Check if file exists using os.path.exists(filename)
    #         Example: if os.path.exists(filename): ...
    #
    # HINT 2: If file exists:
    #         - Open it with: with open(filename, 'r') as f:
    #         - Load JSON: all_results = json.load(f)
    #         (This should give you a list)
    #
    # HINT 3: If file doesn't exist:
    #         - Start with empty list: all_results = []
    #
    # HINT 4: Append the new results: all_results.append(results)
    #
    # HINT 5: Save back to file:
    #         - Open with: with open(filename, 'w') as f:
    #         - Write JSON: json.dump(all_results, f, indent=2)
    #
    # HINT 6: Wrap everything in try/except and return True on success, False on error
    #
    # Example structure:
    #   try:
    #       if os.path.exists(filename):
    #           # Load existing
    #       else:
    #           # Start empty
    #       # Append and save
    #       return True
    #   except Exception:
    #       return False
    
    # ⬇️ REPLACE THE NEXT LINE WITH YOUR CODE ⬇️
    return False
    # ⬇️ WRITE YOUR CODE ABOVE THIS LINE ⬇️


def format_results_text(results: Dict[str, Any]) -> str:
    # ============================================
    # YOUR ANSWER GOES HERE - Write format_results_text function
    # ============================================
    # TODO: Create a nicely formatted text string with all the results
    #
    # HINT 1: Use f-strings to format each line
    #         Example: line1 = f"🔬 Liquid: {results['liquid_name']}"
    #
    # HINT 2: Create multiple lines for:
    #         - Liquid name: results['liquid_name']
    #         - Temperature: results['temperature'] (add °C)
    #         - Pressure: results['pressure'] (add atm)
    #         - State: results['state']
    #         - Freezing point: results['freezing_point'] (add °C)
    #         - Boiling point (normal): results['boiling_point_normal'] (add °C)
    #         - Boiling point (actual): results['boiling_point_actual'] (add °C)
    #
    # HINT 3: Join lines with '\n' (newline) or add '\n' at end of each line
    #         Example: return line1 + '\n' + line2 + '\n' + line3
    #         OR: return f"{line1}\n{line2}\n{line3}"
    #
    # Example structure:
    #   line1 = f"🔬 Liquid: {results['liquid_name']}"
    #   line2 = f"🌡️  Temperature: {results['temperature']}°C"
    #   # ... more lines ...
    #   return line1 + '\n' + line2 + '\n' + ...
    
    # ⬇️ REPLACE THE NEXT LINE WITH YOUR CODE ⬇️
    return "TODO"
    # ⬇️ WRITE YOUR CODE ABOVE THIS LINE ⬇️


