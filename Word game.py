import random

Easy = ["coal", "bird", "mane", "boys"]
Normal = ["string", "python", "lovers"]
Hard = ["touching", "facetious", "exhumation"]
max_attempts = 3


choice = input("Select difficulty (1 = Easy, 2 = Normal, 3 = Hard): ")

if choice == '1':
    word = random.choice(Easy)
elif choice == '2':
    word = random.choice(Normal)
elif choice == '3':
    word = random.choice(Hard)
else:
    print("Error: Invalid choice. Try again.")
    exit()


print(f"Your word is: {word}")
letter_set = set(word)
letter = random.choice(list(letter_set))
wrong_guesses = 0

print("I'm thinking of a letter from the word... can you guess it?")

while wrong_guesses < max_attempts:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess == letter:
        print("🎉 CONGRATULATIONS, you guessed the letter!")
        break
    else:
        wrong_guesses += 1
        print("❌ Nope, not the letter.")
        print(f"Wrong guesses left: {max_attempts - wrong_guesses}")

else:
    print("💀 You've used all your guesses.")
    print(f"The letter was: '{letter}'")

print("Thanks for playing!")
