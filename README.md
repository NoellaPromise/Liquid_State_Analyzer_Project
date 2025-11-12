# 🧪 Liquid State Analyzer - Your Coding Adventure!

Welcome! You're about to build something amazing - a program that can tell you if water (or any liquid) is frozen ❄️, liquid 💧, or boiling 💨 based on temperature and pressure!

## 🎯 What You'll Build

By the end of this project, you'll have created a **Liquid State Analyzer** that:

- Takes temperature and pressure as input
- Decides if a liquid is SOLID, LIQUID, or GAS
- Shows results in a cool web interface with an animated flask!

**The best part?** You'll learn Python programming step by step, one small level at a time!

---

## 📂 What's in This Project?

 you only need to focus on **ONE folder** - the `levels/` folder!

```
📁 Liquid_State_Analyzer_project/
│
├── 📁 levels/              ⭐ THIS IS WHERE YOU WORK!
│   ├── level1_data.py      ← Start here!
│   ├── level2_pressure.py
│   ├── level3_state_logic.py
│   ├── level4_user_io.py
│   └── level5_persist_display.py
│
├── 📁 tests/               🔒 Don't touch these (they check your work!)
├── 📁 backend/             🔒 Don't touch (uses your code after you finish)
├── 📁 frontend/            🔒 Don't touch (the web interface)
├── 📁 data/                📊 Created automatically (you don't need to worry about this)
│
├── 📄 run_levels.py        ← Run this to test your work!
├── 📄 requirements.txt     ← Dependencies (install once)
└── 📄 README.md            ← You're reading this!
```

**Remember:** You only edit files in the `levels/` folder. Everything else is already set up for you!

---

## 🚀 Let's Get Started!

### Step 1: Make Sure Python is Installed

1. Open a terminal/command prompt
2. Type: `python --version`
3. If you see a version number (like 3.8 or higher), you're good! ✅
4. If you get an error, download Python from [python.org](https://python.org)
   - **Important:** Check "Add Python to PATH" when installing!

### Step 2: Install Required Packages

Open terminal/command prompt in this project folder and type:

```bash
pip install -r requirements.txt
```

Wait for it to finish. You only need to do this once!

### Step 3: Test Your Setup

Run this command to see if everything works:

```bash
python run_levels.py
```

You should see all levels showing ❌ FAIL - **that's totally normal!** You haven't completed them yet. Once you finish each level, it will change to ✅ PASS!

---

## 🎮 How to Complete the Levels

### The Game Plan

You'll work through **5 levels**, each one teaching you something new:

| Level       | What You'll Learn   | What You'll Do                                 |
| ----------- | ------------------- | ---------------------------------------------- |
| **Level 1** | Python Dictionaries | Create a list of liquids with their properties |
| **Level 2** | Math & Functions    | Calculate how pressure affects boiling point   |
| **Level 3** | If/Else Logic       | Decide if liquid is SOLID, LIQUID, or GAS      |
| **Level 4** | Input Validation    | Make sure user input is safe and correct       |
| **Level 5** | File Saving         | Save results to a file and format them nicely  |

### How to Complete Each Level

1. **Open the level file** (start with `levels/level1_data.py`)
2. **Read the instructions** at the top of the file
3. **Look for the markers** that say `⬇️ YOUR ANSWER GOES HERE ⬇️`
4. **Fill in your code** where you see the arrows and `# TODO:` comments
5. **Test your work** by running: `python run_levels.py`
6. **Fix any errors** until you see ✅ PASS
7. **Move to the next level!** 🎉



## ✅ Testing Your Work

### Check All Levels at Once

```bash
python run_levels.py
```

This shows you which levels passed ✅ and which need more work ❌.

### Test Just One Level

```bash
python -m tests.test_level1
python -m tests.test_level2
# etc...
```

**Important:** Don't modify files in the `tests/` folder! They check if your code is correct.

---

## 🎉 What Happens After You Complete All Levels?

Once all 5 levels show ✅ PASS, you can run your **complete program**!

### Option 1: Command-Line Version (Terminal)

```bash
python backend/main.py
```

This gives you an interactive program in your terminal where you can:

- Choose a liquid
- Enter temperature and pressure
- See the results!

### Option 2: Web Interface (Cooler!) 🌐

1. **Start the server:**

   ```bash
   python backend/backend_server.py
   ```

   You'll see: `Server running at http://localhost:5000`

2. **Open the web page:**

   - Go to the `frontend/` folder
   - Double-click `index.html`
   - It will open in your browser!

3. **Use your program:**

   - Select a liquid from the dropdown
   - Enter a temperature (like 25 or -10)
   - Enter pressure (or leave it as 1.0)
   - Click "Analyze Liquid State"
   - Watch the flask change! 🧪

4. **Stop the server:** Press `Ctrl+C` in the terminal when you're done

---

## 💡 Tips for Success

1. **Read the hints!** Each level file has helpful hints that guide you step by step
2. **Test often!** Run `python run_levels.py` after every change
3. **Don't panic!** If a test fails, read the error message - it tells you what's wrong!
4. **Ask for help!** Your coach and Colleagues are there to help
5. **Have fun!** Experiment with different values and see what happens!

---

## 🐛 Common Problems & Solutions

### Problem: "Cannot connect to backend server"

**Solution:** Make sure you ran `python backend/backend_server.py` first!

### Problem: "Module not found" error

**Solution:**

- Make sure you're in the project folder
- Try: `pip install -r requirements.txt`

### Problem: Test fails but my code looks right

**Solution:**

- Check for typos (Python is case-sensitive!)
- Make sure you're returning the right type (string vs number)
- Read the error message - it tells you exactly what's wrong!

### Problem: Web page doesn't show liquids

**Solution:**

- Make sure the backend server is running
- Make sure you completed Level 1 (that's where liquids are defined!)

---

## 🎓 What You'll Learn

By completing this project, you'll master:

- ✅ Creating and using Python dictionaries
- ✅ Writing functions with parameters
- ✅ Using if/elif/else for decision making
- ✅ Handling user input safely
- ✅ Reading and writing JSON files
- ✅ Debugging Python code
- ✅ How web applications work (frontend + backend)

---

## 🏆 Success Checklist

You've successfully completed the project when:

- [ ] All 5 levels show ✅ PASS when you run `python run_levels.py`
- [ ] `python backend/main.py` works (command-line version)
- [ ] `python backend/backend_server.py` + web interface works
- [ ] You can explain what each level does
- [ ] You can modify the code and see changes happen!

---

## 🎊 You've Got This!

Remember: Every programmer starts somewhere. Take it one level at a time, test often, and don't be afraid to make mistakes - that's how you learn!

**Ready to start?** Open `levels/level1_data.py` and begin your coding adventure! 🚀

Good luck, and have fun! 🎉
