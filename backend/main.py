"""
Main program that uses the level functions after students complete all TODOs.
Run this only after run_levels.py shows all PASS.
"""

import time
import os
import sys
from typing import Dict, Any

# Add parent directory to path to import levels
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from levels.level1_data import get_default_liquids
from levels.level2_pressure import calculate_pressure_effect
from levels.level3_state_logic import decide_state
from levels.level4_user_io import parse_choice, parse_float, get_pressure_with_default
from levels.level5_persist_display import save_analysis_result, format_results_text


def list_liquids(liquids: Dict[str, Dict[str, Any]]) -> None:
    print("📋 Available liquids:")
    keys = list(liquids.keys())
    for idx, key in enumerate(keys, 1):
        print(f"   {idx}. {liquids[key]['name']}")


def choose_liquid(liquids: Dict[str, Dict[str, Any]]) -> str:
    keys = list(liquids.keys())
    while True:
        choice_str = input(f"\n🔤 Choose a liquid (1-{len(keys)}): ")
        choice = parse_choice(choice_str, len(keys))
        if choice is not None:
            return keys[choice - 1]
        print("❌ Please enter a valid number in range.")


def ask_temperature() -> float:
    while True:
        t_str = input("🌡️  Enter temperature in °C: ")
        t = parse_float(t_str)
        if t is not None:
            return t
        print("❌ Please enter a valid number.")


def ask_pressure() -> float:
    while True:
        p_str = input("📏 Enter atmospheric pressure in atm (press Enter for 1.0): ")
        p = get_pressure_with_default(p_str)
        if p is not None:
            return p
        print("❌ Pressure must be a positive number (or press Enter).")


def build_results(liquid: Dict[str, Any], temperature: float, pressure: float) -> Dict[str, Any]:
    freezing_point = float(liquid["freezing_point"])
    base_boiling_point = float(liquid["boiling_point"])
    actual_boiling_point = float(calculate_pressure_effect(base_boiling_point, pressure))
    state = decide_state(temperature, freezing_point, actual_boiling_point)

    description = {
        "SOLID": f"FROZEN! Temperature {temperature}°C is at or below freezing point ({freezing_point}°C)",
        "GAS": f"BOILING! Temperature {temperature}°C is at or above boiling point ({actual_boiling_point:.1f}°C)",
        "LIQUID": "LIQUID state! Temperature is between freezing and boiling points",
    }[state]

    return {
        "liquid_name": liquid["name"],
        "temperature": temperature,
        "pressure": pressure,
        "state": state,
        "description": description,
        "freezing_point": freezing_point,
        "boiling_point_normal": base_boiling_point,
        "boiling_point_actual": round(actual_boiling_point, 1),
    }


def main() -> None:
    # Ensure data directory exists (in project root, not backend folder)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(project_root, 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    print("🧪 Welcome to Liquid State Analyzer")
    print("=" * 50)
    liquids = get_default_liquids()
    while True:
        list_liquids(liquids)
        choice_key = choose_liquid(liquids)
        temperature = ask_temperature()
        pressure = ask_pressure()

        print("\n🔬 Analyzing liquid state...")
        time.sleep(1)
        results = build_results(liquids[choice_key], temperature, pressure)
        print()
        print(format_results_text(results))

        save_choice = input("\n💾 Save these results? (y/n): ").strip().lower()
        if save_choice == "y":
            ok = save_analysis_result(results)
            print("💾 Results saved." if ok else "❌ Could not save results.")

        cont = input("\n🔄 Analyze another liquid? (y/n): ").strip().lower()
        if cont != "y":
            print("\n🎉 Thank you for using Liquid State Analyzer!")
            print("💡 Remember: Liquids can be STILL, FROZEN, or BOILING!")
            break


if __name__ == "__main__":
    main()


