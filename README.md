# Wordle Solver

## Overview
This program is a simple Wordle solver that uses AI to make educated guesses based on feedback from previous attempts. It starts by randomly selecting a word from a predefined list, then processes feedback (green for correct letters in the right position, yellow for correct letters in the wrong position) to eliminate words that don't fit the criteria. With each guess, the AI refines the list of possible solutions, aiming to solve the puzzle efficiently. The word list is customizable and loaded from a JSON file.

---

## 📂 Project Files
  - [Wordle Solver Program](https://github.com/EricDelgado993/Wordle-Solver/blob/main/Wordle%20Solver%20Project/WordleSolver.py)
  - [Word List](https://github.com/EricDelgado993/Wordle-Solver/blob/main/Wordle%20Solver%20Project/WordList.txt)

---

## Features

### 1. Random Word Selection
- The AI selects a random word from a predefined word list for each guess.

### 2. Feedback Interpretation
- The AI processes feedback based on two types of hints:
  - **Green**: Correct letters in the correct positions.
  - **Yellow**: Correct letters in the wrong positions.

### 3. Word List Pruning
- The AI continuously refines its list of possible words by eliminating options based on feedback:
  - Words containing letters marked as incorrect (gray) are removed.
  - Words that do not match the position of green letters are removed.
  - Words that don't include the yellow letters or have them in the wrong positions are removed.

### 4. Handling of Multiple Character Occurrences
- The AI adjusts its pruning based on the number of occurrences of letters in the guess and feedback:
  - Words that do not match the position of green letters are removed.

### 5. Efficient Word Filtering
- Iteratively filters and reduces the word list after each guess to improve accuracy in future guesses.

### 6. Configurable Word List
- The word list is loaded from a JSON file, allowing for easy updates or customization of the list.
