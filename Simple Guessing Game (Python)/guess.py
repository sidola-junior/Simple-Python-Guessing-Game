# Import module
import random

# Generate random number between 1 to 10.
secret_num = random.randint(1, 10)

lives_count = 0
lives = 3

# Create a loop for the game
while lives_count < lives:
    guess = int(input("I'm thinking of a number between 1 and 10. Have a guess: "))
    lives_count +=1
    if guess == secret_num:
        print('{} was correct!'.format(guess))
        break
else:
    print('Sorry you ran out of lives the correct number was {}'.format(secret_num))
