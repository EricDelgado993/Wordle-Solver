<b>Wordle Solver</b>
<br>This program is a simple Wordle solver that uses AI to make educated guesses based on feedback from previous attempts. It starts by randomly selecting a word from a predefined list, then processes feedback (green for correct letters in the right position, yellow for correct letters in the wrong position) to eliminate words that don't fit the criteria. With each guess, the AI refines the list of possible solutions, aiming to solve the puzzle efficiently. The word list is customizable and loaded from a JSON file.</br>

<br><b>Project Files</b></br>
  - [Wordle Solver Program](https://github.com/EricDelgado993/Wordle-Solver/blob/main/Wordle%20Solver%20Project/WordleSolver.py)
  - [Word List](https://github.com/EricDelgado993/Wordle-Solver/blob/main/Wordle%20Solver%20Project/WordList.txt)

<br><b>Features</b></br>
  - <b>Random World Selection:</b> The AI selects a random word from a predefined word list for each guess.
  - <b>Feedback Interpretation:</b> The AI processes feedback based on two types of hints:
    - <b>Green:</b> Correct letters in the correct positions.
    - <b>Yellow:</b> Correct letters in the wrong positions.
  - <b>Word List Pruning:</b> The AI continuously refines its list of possible words by eliminating options based on feedback:
    - Words containing letters marked as incorrect (gray) are removed.
    - Words that do not match the position of green letters are removed.
    - Words that don't include the yellow letters or have them in the wrong positions are removed.
  - <b>Handling of Multiple Character Occurrences:</b> The AI adjusts its pruning based on the number of occurrences of letters in the guess and feedback:
    - Words that do not match the position of green letters are removed.
  - <b>Efficient Word Filtering:</b> Iteratively filters and reduces the word list after each guess to improve accuracy in future guesses.
  - <b>Configurable Word List:</b> The word list is loaded from a JSON file, allowing for easy updates or customization of the list.
