"""
Tests for Level 4: User Input Helpers
Students should NOT modify this file!
"""

from levels.level4_user_io import parse_choice, parse_float, get_pressure_with_default


def _expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_tests() -> bool:
    print("🔎 Running Level 4 tests...")
    try:
        # parse_choice
        _expect(parse_choice("1", 3) == 1, "parse_choice should accept '1' in [1,3]")
        _expect(parse_choice("3", 3) == 3, "parse_choice should accept '3' in [1,3]")
        _expect(parse_choice("0", 3) is None, "parse_choice should reject 0")
        _expect(parse_choice("4", 3) is None, "parse_choice should reject 4 when max is 3")
        _expect(parse_choice("abc", 3) is None, "parse_choice should reject non-numbers")

        # parse_float
        _expect(parse_float("10") == 10.0, "parse_float should parse integers")
        _expect(parse_float("3.14") == 3.14, "parse_float should parse decimals")
        _expect(parse_float("abc") is None, "parse_float should reject bad input")
        _expect(parse_float("   2.5  ") == 2.5, "parse_float should allow spaces")

        # get_pressure_with_default
        _expect(get_pressure_with_default("") == 1.0, "Empty pressure should default to 1.0")
        _expect(get_pressure_with_default("   ") == 1.0, "Space-only pressure should default to 1.0")
        _expect(get_pressure_with_default("1.2") == 1.2, "Should parse valid positive pressure")
        _expect(get_pressure_with_default("-1") is None, "Should reject non-positive pressure")
        _expect(get_pressure_with_default("abc") is None, "Should reject invalid pressure text")

        print("✅ Level 4 PASSED! Your inputs are safe and sound.")
        return True
    except AssertionError as e:
        print(f"❌ Level 4 FAILED: {e}")
        return False
    except Exception as e:
        print(f"❌ Level 4 ERROR: {e}")
        return False

