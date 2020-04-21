import random

again = 'y'

def roll_dice():
  return random.randint(1, 6)

while again.lower() == 'y':
	# Validation missing, breaks if character is typed
	times = input("How many dices do you want to roll? ")

	for i in range(times):
	  roll = roll_dice()
	  print('Roll: {}').format(roll)

	again = raw_input('Wanna play again? ')