# Project Overview

This is a  learning project that creates a liquid state analyzer web application. It shows different states 
liquids take according to temperature and Atmospheric pressure.

**STILL** 💧: Normal liquid state

**FROZEN** ❄️: Solid state with ice crystals

**BOILING** 💨: Gas state with bubbles and steam

Students will learn backend programming by filling in missing Python code!



Learn the basics of Python [HERE](https://www.w3schools.com/python/python_intro.asp)

Learn The basics of Git and GitHub [HERE](https://docs.github.com/en/get-started)

## Getting Started

### Step 1 : Download and Install VS Code
- Download from [VS Code](https://code.visualstudio.com/)
- Install normally
- Install essential Python extensions
- Set up code formatting and error detection

### Step 2 : Install Python (if not already installed)
- Go to [Python](https://www.python.org/downloads/)
- Click "Download Python" (get version 3.8 or newer)
- **IMPORTANT**: Check "Add Python to PATH" during installation
- Install normally

### Step 3 : Fork Coach's repository
 1. Click on this github link https://github.com/NoellaPromise/Liquid_State_Analyzer_Project
 2. Click the **Fork** button (top-right of the page).  
 3. GitHub will create `https://github.com/your-username/project-name`—this is **your fork**.
 4. Now, Clone your Fork
 5. Open your Terminal (not the VS code terminal)

`# change to a folder where you want to keep class projects`

`cd ~/projects   # or any folder you choose`

`git clone https://github.com/your-username/project-name.git`

`cd project-name`

### Step 4 : Test your Setup

**Open Command Prompt/Terminal in your project folder**
  - Run : `python3 liquid_analyzer.py`  ***This will have errors because you need to fill in the blanks!***



## What you need to fill in
1. **Liquid Data Dictionary**
Complete the `get_default_liquids()` function with liquid properties.

2. **Pressure Calculation**
Fill in the formula to calculate how pressure affects boiling point.

3. **State Logic**
Complete the if/elif/else statements to determine if liquid is solid, liquid, or gas.

4. **File Operations**
Complete the code to save and load results from JSON files.

5. **User Input**
Fill in code to get temperature input from user.

6. **Display Results**
Complete the print statements to show liquid information.


## Assessment Checklist
**You should be able to:**

 - [ ] Explain what dictionaries are and how to use them
 - [ ] Write if/elif/else statements for decision making
 - [ ] Handle user input with error checking
 - [ ] Save and load data from JSON files
 - [ ] Debug common Python errors
 - [ ] Explain how the flask container shows different states
