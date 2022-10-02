#choose your own adventure
name=input('Type your name:')
print('Welcome',name,' to this adventure!')
answer=input('You are on a dirt road ,it has come to an end and you can go left or right.which way would you like to go? ').lower()
if answer=='left':
    answer=input('you come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross:')
    if answer == 'swim':
        print('You swim acrross and eaten by an alligator.')
    elif  answer=='walk':
        print('You walk for many miles, ran out of water and you lost the game!')
    else:
        print('Not a valid options.you lose!')
        
    
elif answer=='right':
    answer=input('You came to a bridge, it looks wobbly, do you want to cross it or head back(cross/back)?')
    if answer == 'back':
        print('You go back  and lose.')
    elif  answer=='cross':
        answer=input('You cross the bridge and meet a stranger.Do you talk them(Yes/no)?')
        if answer=='yes':
            print('You talk to the stringer and they give you gold .You win!')
        elif answer=='no':
            print('You ignore the strenger and they offend and you lose')
        else:
            print('Not a valid options.you lose!')
        
    else:
        print('Not a valid options.you lose!')
        
else:
    print('Not a valid options.you lose!')
print('thank you for trying ',name)