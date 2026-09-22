# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a playable Hangman game in Python that uses user input, loops, conditionals, and string manipulation to track guessed letters and determine whether the player wins or loses.

## 📝 Tasks

### 🛠️ Build the Core Game Loop

#### Description
Create the main gameplay loop for a Hangman game where the player guesses letters to reveal a hidden word.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words
- Show the hidden word as underscores and update it correctly as letters are guessed
- Accept single-letter guesses from the player
- Track which letters have already been guessed
- Reduce the number of remaining attempts when the player guesses incorrectly
- End the game when the word is fully revealed or the player runs out of attempts

### 🛠️ Add Game Feedback and End Conditions

#### Description
Improve the game so the player receives clear feedback during play and understands the result at the end.

#### Requirements
Completed program should:

- Display a message when a guess is correct or incorrect
- Show the current word progress after each guess
- Inform the player when they have already guessed a letter
- Print a win message if the word is completely guessed
- Print a lose message if the player runs out of attempts
- Keep the game easy to follow and readable for the user
