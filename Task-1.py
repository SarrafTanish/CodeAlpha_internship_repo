#-------- Hangman Game--------

import random

# A small predefined list of words to choose from
WORDS = ["python", "hangman", "computer", "keyboard", "science"]

MAX_INCORRECT_GUESSES = 6


def choose_word(word_list):
    """Randomly select a word from the given list."""
    return random.choice(word_list)


def display_progress(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word(WORDS)
    guessed_letters = []
    incorrect_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"Try to guess the word. You have {MAX_INCORRECT_GUESSES} incorrect guesses allowed.")
    print("=" * 40)

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("\nWord: " + display_progress(word, guessed_letters))
        print(f"Incorrect guesses left: {MAX_INCORRECT_GUESSES - incorrect_guesses}")
        if guessed_letters:
            print("Letters guessed so far: " + ", ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 40)
            print(f"Congratulations! You guessed the word: '{word}'")
            print("=" * 40)
            return

    # Player ran out of guesses
    print("\n" + "=" * 40)
    print("You've run out of incorrect guesses. Game over!")
    print(f"The word was: '{word}'")
    print("=" * 40)


def main():
    play_again = "yes"
    while play_again in ("yes", "y"):
        play_hangman()
        play_again = input("\nWould you like to play again? (yes/no): ").lower().strip()

    print("Thanks for playing Hangman!")


if __name__ == "__main__":
    main()