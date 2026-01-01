import random

LOWEST = 1
HIGHEST = 100

DIFFICULTY = {
    "1": ("Easy", 10),
    "2": ("Medium", 5),
    "3": ("Hard", 3),
}

answer = random.randint(LOWEST, HIGHEST)
guesses = 0

print("Python Number Guessing Game")
print(f"Guess a number between {LOWEST} and {HIGHEST}")

choice = input(
    "Select difficulty:\n"
    "1. Easy (10 guesses)\n"
    "2. Medium (5 guesses)\n"
    "3. Hard (3 guesses)\n"
)

if choice not in DIFFICULTY:
    print("Invalid difficulty selected.")
    exit()

level, attempts = DIFFICULTY[choice]
print(f"\nYou selected {level} mode. Let's start!\n")

while attempts > 0:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Invalid input. Enter a number.")
        continue

    guess = int(guess)
    guesses += 1
    attempts -= 1

    if guess < LOWEST or guess > HIGHEST:
        print("Out of range.")
    elif guess < answer:
        print("Too low.")
    elif guess > answer:
        print("Too high.")
    else:
        print(f"\nCorrect! The number was {answer}.")
        print(f"You guessed it in {guesses} attempts.")
        break
else:
    print("You ran out of attempts")
    print(f"\nGame Over! The correct number was {answer}.")
