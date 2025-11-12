"""
Tests for Level 5: Save and Display
Students should NOT modify this file!
"""

import json
import os
from levels.level5_persist_display import save_analysis_result, format_results_text


def _expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_tests() -> bool:
    print("🔎 Running Level 5 tests...")
    temp_file = "test_results.json"
    try:
        # Make sure we start clean
        if os.path.exists(temp_file):
            os.remove(temp_file)

        sample = {
            "liquid_name": "Water (H2O)",
            "temperature": 90.0,
            "pressure": 1.0,
            "state": "LIQUID",
            "description": "Between freezing and boiling",
            "freezing_point": 0.0,
            "boiling_point_normal": 100.0,
            "boiling_point_actual": 100.0,
        }

        # Save test
        saved = save_analysis_result(sample, filename=temp_file)
        _expect(saved is True, "save_analysis_result should return True on success")
        _expect(os.path.exists(temp_file), "File should be created")
        with open(temp_file, "r") as f:
            data = json.load(f)
        _expect(isinstance(data, list) and len(data) >= 1, "File should contain a list with at least one entry")
        _expect(isinstance(data[0], dict), "List entries should be dictionaries")

        # Format test
        text = format_results_text(sample)
        _expect(isinstance(text, str) and len(text) > 0, "format_results_text should return a non-empty string")
        _expect("Liquid" in text and "STATE" in text, "Formatted text should include Liquid and STATE")
        _expect("Temperature" in text and "Pressure" in text, "Formatted text should include Temperature and Pressure")

        print("✅ Level 5 PASSED! Saving and formatting look good.")
        return True
    except AssertionError as e:
        print(f"❌ Level 5 FAILED: {e}")
        return False
    except Exception as e:
        print(f"❌ Level 5 ERROR: {e}")
        return False
    finally:
        # Clean up temp file
        if os.path.exists(temp_file):
            try:
                os.remove(temp_file)
            except Exception:
                pass

