# CODEALPHA INTERNSHIP PROJECT
# TASK 1 - HANGMAN GAME
# Unique Version : Hint Based Hangman

import random

# Word list with hints
words = {
    "python": "Programming Language",
    "elephant": "Largest land animal",
    "cricket": "Popular bat and ball game",
    "computer": "Electronic machine",
    "rainbow": "Appears after rain"
}

# Select random word
word = random.choice(list(words.keys()))
hint = words[word]

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Display hidden word
display_word = ["_"] * len(word)

print("===================================")
print("      WELCOME TO HANGMAN GAME")
print("===================================")

print("\nHint :", hint)

# Game loop
while wrong_guesses < max_wrong and "_" in display_word:

    print("\nWord :", " ".join(display_word))
    print("Wrong Guesses Left :", max_wrong - wrong_guesses)
    print("Guessed Letters :", guessed_letters)

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    # Wrong guess
    else:
        print("Wrong Guess!")
        wrong_guesses += 1

# Result
print("\n===================================")

if "_" not in display_word:
    print("Congratulations! You Won!")
    print("The word was :", word)

else:
    print("Game Over! You Lost!")
    print("Correct word was :", word)

print("===================================")
