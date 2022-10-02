import random
n=input('Enter your number!!')
if n.isdigit():
    n=int(n)
    if n<0:
        print('Please Enter larger then zero next time!! ')
        quit("Try next time!!")
else:
    print('Please type a number next time.!!')
    quit()
winning_number=random.randrange(n)
guess_time=0
print(winning_number)
while True:
    guess_time+=1
    user_guess=input('Make a guess')
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('Please try a number next time')
        continue
    
    if user_guess==winning_number:
        print('You got it')
        
        break
        
    else:
        if user_guess> winning_number:
            print('you are above the number!!')
        else:
            print('you are below the number !!')
print(f'your guess time is {guess_time}')