# 📌 U.S. States Game  

## 📝 Overview  
This is an interactive **U.S. States Guessing Game** using Python and Turtle graphics. The game displays a blank map of the U.S., and the player must type in state names to correctly label them on the map. The game tracks correct guesses and saves unguessed states to a file for future learning.

---

## 🚀 How to Play  
1. Run the script using Python.  
2. A U.S. map will appear.  
3. Type the name of a state in the input box and press **Enter**.  
4. If the state is correct, it will appear on the map.  
5. Continue guessing until all 50 states are labeled or type **"Exit"** to quit.  
6. When you exit, a file `states_to_learn.csv` is created with the states you missed.  

---

## 🛠 Requirements  
Ensure you have Python installed along with the required libraries:  
```bash
pip install pandas turtle
```

---

## 📂 File Structure  
```
|-- us_states_game.py  # Main game script
|-- blank_states_img.gif  # U.S. map image
|-- 50_states.csv  # CSV file containing state names and coordinates
|-- states_to_learn.csv  # File generated for unguessed states
```

---

## 🏆 Features  
✅ Interactive input for guessing states  
✅ Dynamically updates correct guesses on the map  
✅ Prevents duplicate guesses  
✅ Saves missed states for future learning  

---

## 🖥 Running the Game  
Run the Python script:  
```bash
python us_states_game.py
```

---

## 🎯 Future Improvements  
- Add a timer for challenge mode ⏳  
- Provide hints when the user is stuck 🧠  
- Implement a leaderboard for multiple attempts 🏅  

---

Enjoy the game and test your U.S. geography knowledge! 🌍🎮
