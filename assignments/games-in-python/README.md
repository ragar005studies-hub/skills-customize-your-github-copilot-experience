
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game in Python that reinforces string manipulation, control flow, and user interaction.

## 📝 Tasks

### 🛠️ Core: Implement Hangman

#### Description
Create a terminal-based Hangman game where the program randomly selects a secret word and the player guesses letters until they either discover the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Prompt the player to guess single letters and update the displayed word progress (e.g., `_ _ a _ _`).
- Track and display guessed letters and remaining incorrect attempts.
- Prevent repeated guesses from affecting remaining attempts.
- End the game with a clear win or lose message and reveal the secret word when the player loses.

### 🛠️ Optional: Enhancements (stretch goals)

#### Description
Add one or more quality-of-life or feature improvements to the core game.

#### Requirements (pick any)

- Add difficulty levels that change `max_incorrect` or word lists.
- Add scoring or a high-score file to persist best results.
- Support guessing the full word as an action.
- Improve user interface (clear screen between turns, show hangman ASCII art).

## 📁 Files

- Starter code: [assignments/games-in-python/starter-code.py](assignments/games-in-python/starter-code.py)

## 🚀 How to run

Run the starter script with Python 3:

```bash
python3 assignments/games-in-python/starter-code.py
```

If you implement functions or split code across modules, ensure the main entry point still runs with the command above.

## ⏱️ Estimated Time & Difficulty

- Difficulty: Beginner / Intermediate
- Estimated time: 60–120 minutes depending on chosen enhancements

## ✅ Submission checklist

- Program runs without syntax errors.
- Core requirements are implemented and tested manually.
- Optional enhancements (if any) are documented in this README.

