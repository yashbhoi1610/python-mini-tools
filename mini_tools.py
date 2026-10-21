
import random
import re
from collections import Counter


def guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")
    secret_number = random.randint(1, 100)
    attempts = 0
    score = 100

    print("Guess a number between 1 and 100!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Enter a whole number.")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            score = max(0, score - 10)
            print("Too low! Try again.")
        elif guess > secret_number:
            score = max(0, score - 10)
            print("Too high! Try again.")
        else:
            print(f"Correct! The number was {secret_number}.")
            print(f"Attempts: {attempts}")
            print(f"Final score: {score}")
            break


def word_frequency():
    print("\n--- WORD FREQUENCY ANALYZER ---")
    filename = input("Enter text filename (default: sample.txt): ").strip()

    if not filename:
        filename = "sample.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
    except (OSError, UnicodeError):
        print("Could not read the file. Check its name and try again.")
        return

    words = re.findall(r"\b[a-zA-Z0-9']+\b", text.lower())

    if not words:
        print("The file is empty or contains no readable words.")
        return

    word_counts = Counter(words)

    print(f"\nTotal words: {len(words)}")
    print(f"Unique words: {len(word_counts)}")
    print("\nTop 10 most common words:")

    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")


def main():
    while True:
        print("\n===== PYTHON MINI TOOLS =====")
        print("1. Number Guessing Game")
        print("2. Word Frequency Analyzer")
        print("3. Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            guessing_game()
        elif choice == "2":
            word_frequency()
        elif choice == "3":
            print("Thanks for using Python Mini Tools!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
