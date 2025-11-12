"""
Run all level self-checks.

Use this after students have worked through each level to see a quick scoreboard.
Tests are in the tests/ folder - students should NOT modify those!
"""

from importlib import import_module

TEST_MODULES = [
    "tests.test_level1",
    "tests.test_level2",
    "tests.test_level3",
    "tests.test_level4",
    "tests.test_level5",
]


def main() -> None:
    print("\n🧪 Liquid State Analyzer - Level Checks\n" + "=" * 50)
    print("📝 Tests are in tests/ folder - don't modify them!\n")
    all_passed = True
    for mod_name in TEST_MODULES:
        try:
            mod = import_module(mod_name)
            passed = bool(getattr(mod, "run_tests")())
            status = "✅ PASS" if passed else "❌ FAIL"
            level_num = mod_name.split("test_level")[1]
            print(f"Level {level_num}: {status}")
            all_passed = all_passed and passed
        except Exception as e:
            level_num = mod_name.split("test_level")[1] if "test_level" in mod_name else "?"
            print(f"Level {level_num}: ❌ ERROR ({e})")
            all_passed = False

    print("=" * 50)
    if all_passed:
        print("🎉 All levels passed! You can now:")
        print("   1. Run command-line version: python main.py")
        print("   2. Run web version: python backend_server.py")
        print("      Then open index.html in your browser!")
    else:
        print("🔧 Some levels failed. Open the level file and complete the TODOs.")
        print("   Example: levels/level1_data.py")


if __name__ == "__main__":
    main()


