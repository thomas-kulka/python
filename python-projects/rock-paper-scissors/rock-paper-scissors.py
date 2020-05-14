import random

options = ['rock', 'paper', 'scissors']

user_selection = None
AI_selection = random.choice(options)

print("Select: rock .:|:. paper .:|:. scissors")

# Make sure user types correct value
while user_selection == None:
  user_selection = input('Your pick: ').lower()
  
  if user_selection not in options:
    print('Select from available options!')
    user_selection = None

# logic for different combinations
if user_selection == AI_selection:
  print('The game is drawn.')
elif user_selection == 'rock':
  if AI_selection == 'paper':
    print('AI wins.')
  else:
    print('You won!')
elif user_selection == 'paper':
  if AI_selection == 'scissors':
    print('AI wins.')
  else:
    print('You won!')
elif AI_selection == 'rock':
  print('AI wins.')
else:
  print('You won!')
  
print('AI selected: {}'.format(AI_selection))
print('You selected: {}'.format(user_selection))