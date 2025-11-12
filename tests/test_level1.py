"""
Tests for Level 1: Liquid Data
Students should NOT modify this file!
"""

from levels.level1_data import get_default_liquids


def _expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_tests() -> bool:
    print("🔎 Running Level 1 tests...")
    try:
        data = get_default_liquids()
        _expect(isinstance(data, dict), "get_default_liquids() must return a dict")
        _expect(len(data) >= 3, "Please add at least 3 liquids")

        # Required: water and ethanol with correct points
        _expect("water" in data, "Please include a 'water' entry")
        _expect("ethanol" in data, "Please include an 'ethanol' entry")

        water = data["water"]
        _expect(isinstance(water, dict), "'water' value must be a dict")
        _expect("name" in water and "freezing_point" in water and "boiling_point" in water,
                "'water' must have name, freezing_point, and boiling_point")
        _expect(abs(float(water["freezing_point"]) - 0.0) < 1e-6, "Water freezing_point should be 0.0")
        _expect(abs(float(water["boiling_point"]) - 100.0) < 1e-6, "Water boiling_point should be 100.0")

        ethanol = data["ethanol"]
        _expect(isinstance(ethanol, dict), "'ethanol' value must be a dict")
        _expect("name" in ethanol and "freezing_point" in ethanol and "boiling_point" in ethanol,
                "'ethanol' must have name, freezing_point, and boiling_point")
        _expect(abs(float(ethanol["freezing_point"]) - (-114.1)) < 1e-6,
                "Ethanol freezing_point should be -114.1")
        _expect(abs(float(ethanol["boiling_point"]) - 78.4) < 1e-6,
                "Ethanol boiling_point should be 78.4")

        print("✅ Level 1 PASSED! Great job on the data setup.")
        return True
    except AssertionError as e:
        print(f"❌ Level 1 FAILED: {e}")
        return False
    except Exception as e:
        print(f"❌ Level 1 ERROR: {e}")
        return False

