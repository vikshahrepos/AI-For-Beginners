import random

HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """,
]

WORDS = [
    "python",
    "computer",
    "science",
    "hangman",
    "artificial",
    "intelligence",
]


def get_display_word(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play_hangman():
    random.seed(0)
    word = random.choice(WORDS)
    guessed = set()
    wrong = set()
    max_attempts = len(HANGMAN_STAGES) - 1

    while len(wrong) < max_attempts:
        print(HANGMAN_STAGES[len(wrong)])
        print("Word:", get_display_word(word, guessed))
        print(f"Wrong guesses: {' '.join(sorted(wrong)) if wrong else 'None'}")
        guess = input("Guess a letter: ").lower()

        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.\n")
            continue
        if guess in guessed or guess in wrong:
            print("You already guessed that letter.\n")
            continue

        if guess in word:
            guessed.add(guess)
            if all(letter in guessed for letter in word):
                print(f"Congratulations! You guessed the word '{word}'.")
                return
        else:
            wrong.add(guess)
            print("Incorrect!\n")

    print(HANGMAN_STAGES[-1])
    print(f"Sorry, you ran out of attempts. The word was '{word}'.")


if __name__ == "__main__":
    play_hangman()
