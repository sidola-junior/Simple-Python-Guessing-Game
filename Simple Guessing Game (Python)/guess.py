# importing module
from random import randint

# Ask user for name
name = input('What is your name? ') 

# Game instructions
print("\nHey there {}, you have three lives to guess a number I'm thinking of between 1 and 10. Good Luck!".format(name.title()))

# generating random secret number between 1 and 10.
secret_num = randint(1,10)

# variables for game
lives = 0

# creating game 
while lives < 3:
  # player input here
  guess = int(input('\nI am thinking of number between 1 and 10: '))
  # actual game loop here
  if guess == secret_num:
    break
  else:
    print('\nIncorrect, Guess Again!')
    lives += 1

# End game message to player   
if guess == secret_num:
  print("\nThat's correct!, Well done!")
else:
  print("Sorry the correct answer was: {}".format(str(secret_num)))
