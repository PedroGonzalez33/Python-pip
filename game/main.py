import random

# Rock, Paper, Scissors gameUser choice: {user_value}\nPc Choice {pc_value}\nPc Win

games = 0
user_Win = 0
pc_Win = 0

print('Welcome to this game: Rock, Paper, Scissors.\nBest of 5 games win')

def chose():
  while True:
    user_value = input().lower()
    pc_value = random.choice(('rock', 'paper', 'scissors'))

    if (user_value == 'rock') or (user_value == 'paper') or (user_value == 'scissors'):
     break

    print('Please introduce a valid value')

  return user_value, pc_value 

def game(user_value, pc_value, games, user_Win, pc_Win):
 
  if user_value == pc_value:
    games += 1
    print(f'\nUser choice: {user_value}\nPc Choice {pc_value}\nGame Draw')
    
  elif (user_value == 'rock' and pc_value == 'scissors') or (user_value == 'paper' and pc_value == 'rock') or (user_value == 'scissors' and pc_value == 'paper'):
    user_Win += 1
    games += 1
    print(f'\nUser choice: {user_value}\nPc Choice: {pc_value}\nUser Win')
  
  elif (pc_value == 'rock' and user_value == 'scissors') or (pc_value == 'paper' and user_value == 'rock') or (pc_value == 'scissors' and user_value == 'paper'):
    pc_Win += 1
    games += 1
    print(f'\nUser choice: {user_value}\nPc Choice: {pc_value}\nPc Win')
  
  return user_Win, pc_Win, games

def who_win(user_Win, pc_Win):
  if user_Win > pc_Win:
    print('\nUser win: ', user_Win,'\nPc win: ', pc_Win, '\nYou win!! Congratulations')

  elif pc_Win > user_Win:
    print('\nUser win: ', user_Win,'\nPc win: ', pc_Win, '\nYou lose :( Best luck next time')

  elif user_Win == pc_Win:
    print('\nUser win: ', user_Win,'\nPc win: ', pc_Win, '\nGame is draw')

while games < 5:
  print('\nChose one: Rock, Paper or Scissors')
  user_value, pc_value = chose()
  user_Win, pc_Win, games = game(user_value, pc_value, games, user_Win, pc_Win)

who_win(user_Win, pc_Win)