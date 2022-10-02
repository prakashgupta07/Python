#Rock paper scissors

import random
user_wins=0
computer_wins=0
options=['rock','paper','scissors']
while True:
    user_input=input('Type Rock/Paper/Scissors or Q to quit:').lower()
    if user_input=='q':
        quit('quit')
    if user_input not in options:
        continue
    random_number=random.randint(0, 2)
    computer_pick=options[random_number]
    print('computer pick',computer_pick)
    
    if user_input=='rock' and( computer_pick=='paper' or computer_pick=='scissors'):
        print( 'you win!!')
        user_wins+=1
    elif user_input=='paper' and( computer_pick=='rock' or computer_pick=='scissors'):
        print('you win!!')
        user_wins+=1
    elif user_input=='scissors' and( computer_pick=='paper' or computer_pick=='rock'):
        print('You win!!')
        user_wins+=1
    else:
        print('You lose!!')
        computer_wins+=1

print(f' you win {user_wins} times')
print(f'computer wins {computer_wins} times')
print('Goodbye')