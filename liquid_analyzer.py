#!/usr/bin/env python3
"""
Liquid State Analyzer - STUDENT VERSION (Fill in the blanks)
Grade 8 Coding Club Project - NLS
Fill in the missing code where you see: # TODO: [instructions]
"""

import json
import os
import webbrowser
import time

class LiquidAnalyzer:
    """This class analyzes liquid states like a smart chemistry calculator"""
    
    def __init__(self):
        """This runs when we create a new LiquidAnalyzer"""
        print("🧪 Starting Liquid State Analyzer...")
        self.liquids_data = self.load_liquid_data()
        
        self.flask_art = {
            "still": """
    LIQUID (Still)
         ___
        |   |
        |   |
      __|___|__
     |         |
     |  ~~~~~  |   💧
     |  ~~~~~  |
     |  ~~~~~  |
     |_________|
            """,
            "frozen": """
    SOLID (Frozen) 
         ___
        |   |
        |   |
      __|___|__
     |         |
     |  ❄️ ❄️ ❄️ |   🧊
     |  ❄️ ❄️ ❄️ |
     |  ❄️ ❄️ ❄️ |
     |_________|
            """,
            "boiling": """
    GAS (Boiling)
         ___     💨 💨
        | ° |  💨  💨 💨
        | ° |   💨  💨
      __|°__|__ 💨  💨
     |    °    |
     |  ° ° °  |   🔥
     | ° ° ° ° |
     | ° ° ° ° |
     |_________|
            """
        }
    
    def load_liquid_data(self):
        """Load liquid information from JSON file"""
        try:
            with open('liquids_data.json', 'r') as file:
                data = json.load(file)
                print("✅ Loaded liquid data from liquids_data.json")
                return data
        except FileNotFoundError:
            print("📄 Creating liquids_data.json with default data...")
            default_data = self.get_default_liquids()
            self.save_liquid_data(default_data)
            return default_data
    
    def get_default_liquids(self):
        """Return default liquid data"""
        
        # TODO: Fill in the liquid data dictionary with at least 3 liquids
        # TODO: Each liquid should have: name, freezing_point, boiling_point
        # TODO: Example: "water": {"name": "Water (H₂O)", "freezing_point": 0.0, "boiling_point": 100.0}
        
        return {
            # TODO: Add water data here
            
            
            # TODO: Add ethanol data here (freezing: -114.1, boiling: 78.4)
            
            
            # TODO: Add at least one more liquid of your choice
            
            
        }
    
    def save_liquid_data(self, data):
        """Save liquid data to JSON file"""
        with open('liquids_data.json', 'w') as file:
            json.dump(data, file, indent=2)
        print("💾 Saved liquid data to liquids_data.json")
    
    def get_available_liquids(self):
        """Get list of available liquids"""
        return self.liquids_data
    
    def calculate_pressure_effect(self, base_boiling_point, pressure):
        """Calculate how pressure affects boiling point"""
        
        # TODO: Calculate adjusted boiling point
        # TODO: Formula: each 1 atm change affects boiling by 10°C
        # TODO: Hint: pressure_difference = pressure - 1.0 (standard pressure)
        # TODO: Hint: adjusted_boiling = base_boiling_point + (pressure_difference * 10.0)
        
        pressure_difference = # TODO: Fill this in
        adjusted_boiling = # TODO: Fill this in
        
        return adjusted_boiling
    
    def analyze_liquid_state(self, temperature, pressure, liquid_type):
        """Main function that analyzes liquid state"""
        
        if liquid_type not in self.liquids_data:
            raise ValueError(f"Unknown liquid: {liquid_type}")
        
        if pressure <= 0:
            raise ValueError("Pressure must be greater than 0")
        
        liquid = self.liquids_data[liquid_type]
        freezing_point = liquid["freezing_point"]
        base_boiling_point = liquid["boiling_point"]
        
        actual_boiling_point = self.calculate_pressure_effect(base_boiling_point, pressure)
        
        # TODO: Determine liquid state using if/elif/else
        # TODO: If temperature <= freezing_point: it's SOLID (frozen)
        # TODO: If temperature >= actual_boiling_point: it's GAS (boiling)  
        # TODO: Otherwise: it's LIQUID (still)
        
        if # TODO: Fill in condition for frozen state
            state = "SOLID"
            flask_state = "frozen"
            description = f"FROZEN! Temperature {temperature}°C is at or below freezing point ({freezing_point}°C)"
            
        elif # TODO: Fill in condition for boiling state
            state = "GAS"
            flask_state = "boiling"
            description = f"BOILING! Temperature {temperature}°C is at or above boiling point ({actual_boiling_point:.1f}°C)"
            
        else:
            # TODO: Fill in the liquid state information
            state = # TODO: What should this be?
            flask_state = # TODO: What should this be?
            description = f"LIQUID state! Temperature is between freezing and boiling points"
        
        return {
            "liquid_name": liquid["name"],
            "temperature": temperature,
            "pressure": pressure,
            "state": state,
            "flask_state": flask_state,
            "description": description,
            "freezing_point": freezing_point,
            "boiling_point_normal": base_boiling_point,
            "boiling_point_actual": round(actual_boiling_point, 1),
            "flask_art": self.flask_art[flask_state]
        }
    
    def save_analysis_result(self, results):
        """Save analysis results to JSON file"""
        import datetime
        results_with_time = results.copy()
        results_with_time['analysis_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if 'flask_art' in results_with_time:
            del results_with_time['flask_art']
        
        # TODO: Load existing results from file if it exists
        # TODO: Hint: Check if 'analysis_results.json' exists using os.path.exists()
        # TODO: If it exists, load it. If not, create an empty list.
        
        if os.path.exists('analysis_results.json'):
            # TODO: Open file and load existing results
            with open('analysis_results.json', 'r') as file:
                all_results = # TODO: Load JSON data here
        else:
            # TODO: Create empty list for new results
            all_results = # TODO: What should this be?
        
        all_results.append(results_with_time)
        
        with open('analysis_results.json', 'w') as file:
            json.dump(all_results, file, indent=2)
        
        print("💾 Results saved to analysis_results.json")

def display_results(results):
    """Display results in a nice format"""
    print("\n" + "="*60)
    print("🧪 LIQUID STATE ANALYSIS RESULTS 🧪")
    print("="*60)
    
    # TODO: Print the liquid information
    # TODO: Print liquid name, temperature, pressure, and state
    # TODO: Use the format: print(f"🔬 Liquid: {results['liquid_name']}")
    
    print(f"🔬 Liquid: # TODO: Fill this in")
    print(f"🌡️  Temperature: # TODO: Fill this in")
    print(f"📏 Pressure: # TODO: Fill this in")
    print(f"\n🏷️  STATE: # TODO: Fill this in")
    
    print(results['flask_art'])
    
    print("📖 EXPLANATION:")
    print(f"   {results['description']}")
    
    print(f"\n📊 REFERENCE POINTS:")
    print(f"   • Freezing point: {results['freezing_point']}°C")
    print(f"   • Boiling point (1 atm): {results['boiling_point_normal']}°C")
    print(f"   • Boiling point (current pressure): {results['boiling_point_actual']}°C")
    
    print("="*60)

def get_user_input():
    """Get input from user with simple prompts"""
    print("\n🎯 Let's analyze a liquid state!")
    print("🧪 The flask will show: STILL (liquid), FROZEN (solid), or BOILING (gas)")
    print()
    
    analyzer = LiquidAnalyzer()
    liquids = analyzer.get_available_liquids()
    
    print("📋 Available liquids:")
    liquid_list = list(liquids.keys())
    for i, liquid_key in enumerate(liquid_list, 1):
        liquid_info = liquids[liquid_key]
        print(f"   {i}. {liquid_info['name']}")
    
    # TODO: Get liquid choice from user
    # TODO: Use a while loop to keep asking until valid input
    # TODO: Convert user input to integer and check if it's in valid range
    while True:
        try:
            choice = input(f"\n🔤 Choose a liquid (1-{len(liquid_list)}): ")
            choice_num = int(choice)
            if 1 <= choice_num <= len(liquid_list):
                liquid_type = liquid_list[choice_num - 1]
                break
            else:
                print(f"❌ Please enter a number between 1 and {len(liquid_list)}")
        except ValueError:
            print("❌ Please enter a valid number")
    
    # TODO: Get temperature from user
    # TODO: Use a while loop and try/except to handle invalid input
    while True:
        try:
            temperature = # TODO: Get temperature input and convert to float
            break
        except ValueError:
            print("❌ Please enter a valid number")
    
    # TODO: Get pressure from user (with default value of 1.0)
    # TODO: If user presses Enter without typing, use 1.0
    while True:
        try:
            pressure_input = input("📏 Enter atmospheric pressure in atm (press Enter for 1.0): ")
            if pressure_input.strip() == "":
                pressure = 1.0
            else:
                pressure = float(pressure_input)
            
            if pressure > 0:
                break
            else:
                print("❌ Pressure must be greater than 0")
        except ValueError:
            print("❌ Please enter a valid number")
    
    return temperature, pressure, liquid_type

def main():
    """Main program function"""
    try:
        print("🧪 Welcome to Liquid State Analyzer - Student Version!")
        print("=" * 50)
        
        analyzer = LiquidAnalyzer()
        
        # TODO: Create a loop that continues until user wants to stop
        # TODO: Use while True: and break when user doesn't want to continue
        
        while True:
            temperature, pressure, liquid_type = get_user_input()
            
            print("\n🔬 Analyzing liquid state...")
            time.sleep(1)
            
            # TODO: Call the analyze_liquid_state method
            results = analyzer.analyze_liquid_state(temperature, pressure, liquid_type)
            
            display_results(results)
            
            
            # TODO: Ask user if they want to save results
            save_choice = input("\n💾 Save these results? (y/n): ").lower()
            if save_choice == 'y':
                # TODO: Call the save method
                # TODO: Fill this in
            
            # TODO: Ask user if they want to continue
            continue_choice = input("\n🔄 Analyze another liquid? (y/n): ").lower()
            
            if # TODO: Fill in condition to break loop
                print("\n🎉 Thank you for using Liquid State Analyzer!")
                print("💡 Remember: Liquids can be STILL, FROZEN, or BOILING!")
                break
    
    
    
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Thanks for using Liquid State Analyzer!")
    except Exception as error:
        print(f"\n❌ Something went wrong: {error}")
        print("🔧 Please check your input and try again.")

if __name__ == "__main__":
    main()