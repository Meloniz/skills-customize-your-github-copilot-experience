# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input to create an interactive word-guessing experience.

## 📝 Tasks

### 🛠️ Create the Game Logic

#### Description
Write the core logic for a Hangman game that selects a hidden word and tracks the player's guesses.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list
- Display the hidden word as blanks such as `_ _ _`
- Accept a single letter guess from the player
- Reveal correctly guessed letters in the word
- Keep track of incorrect guesses and remaining attempts

### 🛠️ Add Game Flow and Win/Lose Conditions

#### Description
Implement the main game loop so the player continues guessing until the word is solved or the game ends.

#### Requirements
Completed program should:

- Continue prompting the player until they guess the word or run out of attempts
- Notify the player when a guess is correct or incorrect
- End the game when the player wins or loses
- Display a clear win message or game-over message

### 🛠️ Improve the User Experience

#### Description
Polish the game's interaction by making the output clear and easy to follow during play.

#### Requirements
Completed program should:

- Show the guessed letters so far
- Display the number of attempts remaining
- Handle repeated guesses gracefully
- Use simple, readable console output that helps the player play the game
