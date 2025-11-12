"""
Tests for Level 3: State Logic
Students should NOT modify this file!
"""

from levels.level3_state_logic import decide_state


def run_tests() -> bool:
    print("🔎 Running Level 3 tests...")
    try:
        # Use water reference points at 1.0 atm
        freeze = 0.0
        boil = 100.0
        # Boundaries
        assert decide_state(-5.0, freeze, boil) == "SOLID", "Below freezing should be SOLID"
        assert decide_state(0.0, freeze, boil) == "SOLID", "At freezing should be SOLID"
        assert decide_state(100.0, freeze, boil) == "GAS", "At boiling should be GAS"
        assert decide_state(101.0, freeze, boil) == "GAS", "Above boiling should be GAS"
        assert decide_state(50.0, freeze, boil) == "LIQUID", "Between freezing and boiling should be LIQUID"

        print("✅ Level 3 PASSED! Great conditional thinking.")
        return True
    except AssertionError as e:
        print(f"❌ Level 3 FAILED: {e}")
        return False
    except Exception as e:
        print(f"❌ Level 3 ERROR: {e}")
        return False

