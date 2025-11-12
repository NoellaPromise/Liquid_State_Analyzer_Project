"""
Backend Server for Liquid State Analyzer Web Interface

This connects the student's completed level functions to the frontend.
Run this after completing all levels: python backend_server.py
Then open index.html in your browser!
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import sys
from typing import Dict, Any

# Add parent directory to path to import levels
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import student functions from levels
from levels.level1_data import get_default_liquids
from levels.level2_pressure import calculate_pressure_effect
from levels.level3_state_logic import decide_state

app = Flask(__name__)
CORS(app)  # Allow frontend to call this API


@app.route('/api/liquids', methods=['GET'])
def get_liquids():
    """Return list of available liquids"""
    try:
        liquids = get_default_liquids()
        # Convert to list format for frontend
        result = []
        for key, value in liquids.items():
            result.append({
                "key": key,
                "name": value["name"]
            })
        return jsonify({"success": True, "liquids": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/analyze', methods=['POST'])
def analyze_liquid():
    """Analyze liquid state based on temperature, pressure, and liquid type"""
    try:
        data = request.json
        temperature = float(data.get('temperature'))
        pressure = float(data.get('pressure', 1.0))
        liquid_type = data.get('liquid')

        if pressure <= 0:
            return jsonify({"success": False, "error": "Pressure must be greater than 0"}), 400

        # Get liquid data
        liquids = get_default_liquids()
        if liquid_type not in liquids:
            return jsonify({"success": False, "error": f"Unknown liquid: {liquid_type}"}), 400

        liquid = liquids[liquid_type]
        freezing_point = float(liquid["freezing_point"])
        base_boiling_point = float(liquid["boiling_point"])

        # Calculate actual boiling point with pressure
        actual_boiling_point = calculate_pressure_effect(base_boiling_point, pressure)

        # Determine state
        state = decide_state(temperature, freezing_point, actual_boiling_point)

        # Build description
        if state == "SOLID":
            description = f"FROZEN! Temperature {temperature}°C is at or below freezing point ({freezing_point}°C)"
            flask_state = "frozen"
        elif state == "GAS":
            description = f"BOILING! Temperature {temperature}°C is at or above boiling point ({actual_boiling_point:.1f}°C)"
            flask_state = "boiling"
        else:
            description = "LIQUID state! Temperature is between freezing and boiling points"
            flask_state = "still"

        result = {
            "liquid_name": liquid["name"],
            "temperature": temperature,
            "pressure": pressure,
            "state": state,
            "flask_state": flask_state,
            "description": description,
            "freezing_point": freezing_point,
            "boiling_point_normal": base_boiling_point,
            "boiling_point_actual": round(actual_boiling_point, 1)
        }

        # Optionally save result
        try:
            from levels.level5_persist_display import save_analysis_result
            save_analysis_result(result)
        except Exception:
            pass  # Don't fail if save doesn't work

        return jsonify({"success": True, "result": result})

    except ValueError as e:
        return jsonify({"success": False, "error": f"Invalid input: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/results', methods=['GET'])
def get_saved_results():
    """Get all saved analysis results"""
    try:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_file = os.path.join(project_root, 'data', 'analysis_results.json')
        if os.path.exists(data_file):
            with open(data_file, 'r') as f:
                results = json.load(f)
            return jsonify({"success": True, "results": results})
        else:
            return jsonify({"success": True, "results": []})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    # Ensure data directory exists (in project root, not backend folder)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(project_root, 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    print("🚀 Starting Liquid State Analyzer Backend Server...")
    print("📝 Make sure you've completed all levels first!")
    print("🌐 Server running at http://localhost:5000")
    print("📄 Open frontend/index.html in your browser to use the web interface")
    print("🛑 Press Ctrl+C to stop the server\n")
    app.run(debug=True, port=5000)

