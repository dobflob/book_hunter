# Phrase Hunter
A simple guessing game to practice Python classes.

## Before the First Guess
For each run of the game, a random phrase should be selected from a list of phrases (no punctuation, numbers, or special characters in a phrase) with 2 or more words.

Before a player has made their first guess, the active phrase should be displayed to the player with underscore placeholders. Any spaces between words in the phrase must be clearly visible to the player.

## Prompting for a Guess
The game must prompt the player for a guess on every turn

## Guessing Logic
After every guess, the game should check whether the guessed letter is in the active phrase:
- After every correct guess, the underscored phrase should be displayed again with any correctly guessed letters in place of the associated underscore
- After every incorrect guess, the number missed should increase by 1 (game over when incorrect guesses = 5)