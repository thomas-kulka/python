import random

repeat_game = True

def dice_roll():
  result = random.randint(1,6)
  return result
  
def percent_chance(dice1, dice2):
  probability = ["2.78%", "5.56%", "8.33%", "11.11%", "13.89%", "16.67%", "13.89%", "11.11%", "8.33%", "5.56%", "2.78%"]
  return probability[(dice1 + dice2 - 2)]
  
while repeat_game:
  first_roll = dice_roll()
  second_roll = dice_roll()
  
  chance = percent_chance(first_roll, second_roll)
  
  print('You rolled: {} and {}').format(first_roll, second_roll)
  print('Probability of throwing any given total: {}').format(chance)
  # raw_input is python 2.7.x function
  repeat_game = ('y' or 'yes') in raw_input('Play again? Type y or yes\n').lower()
