import random

number = random.randint(1, 100)
attempts = 5

print("Guess the number between 1 and 100. You have", attempts, "attempts.")

for i in range(attempts):
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it right.")
        break
else:
    print("Sorry, you've used all your attempts. The number was:", number)
