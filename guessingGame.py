import random

n = random.randint(1,9)

print(n)

while chances < 5:

    if guess - n > 2:
        print("Guess less than", number)

    if guess - n < 2:
        print("Guess higher than", number)

    if guess == number:
        print("Congratulations! You WONNNN :)))  <3")
        break

    if not chances<5:
        print("You LOSE! The correct number is", number)


