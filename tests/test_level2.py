"""
Tests for Level 2: Pressure Effect
Students should NOT modify this file!
"""

from levels.level2_pressure import calculate_pressure_effect


def _close(a: float, b: float, tol: float = 1e-6) -> bool:
    return abs(a - b) < tol


def run_tests() -> bool:
    print("🔎 Running Level 2 tests...")
    try:
        base = 100.0
        assert calculate_pressure_effect(base, 1.0) is not None, "Return a number, not None"

        a = calculate_pressure_effect(base, 1.0)
        b = calculate_pressure_effect(base, 1.5)
        c = calculate_pressure_effect(base, 0.5)
        d = calculate_pressure_effect(base, 2.0)

        assert _close(a, 100.0), "At 1.0 atm, boiling point should stay the same"
        assert _close(b, 105.0), "At 1.5 atm, +5°C"
        assert _close(c, 95.0), "At 0.5 atm, -5°C"
        assert _close(d, 110.0), "At 2.0 atm, +10°C"

        print("✅ Level 2 PASSED! Nice pressure math.")
        return True
    except AssertionError as e:
        print(f"❌ Level 2 FAILED: {e}")
        return False
    except Exception as e:
        print(f"❌ Level 2 ERROR: {e}")
        return False

