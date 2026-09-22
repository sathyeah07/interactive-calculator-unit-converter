import random
from collections import Counter


def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    print("I have selected a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print("Correct!")
                print("You guessed it in", attempts, "attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")


def word_counter():
    print("\n--- Word Counter ---")

    filename = input("Enter the text file name: ")

    try:
        with open(filename, "r") as file:
            text = file.read()

        words = text.lower().split()
        total_words = len(words)

        frequency = Counter(words)

        print("\nTotal words:", total_words)
        print("\nWord Frequency:")

        for word, count in frequency.most_common():
            print(word, ":", count)

    except FileNotFoundError:
        print("File not found. Please check the filename.")


while True:
    print("\n==============================")
    print(" Number Guessing Game")
    print(" & Word Counter")
    print("==============================")
    print("1. Number Guessing Game")
    print("2. Word Counter")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number_guessing_game()

    elif choice == "2":
        word_counter()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
