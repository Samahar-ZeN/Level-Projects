#..............................Guessing_Game_Python.....................................#


print('Lets Start Guessing Game!')
print('Its going to be so amazing Game for you!😁')
print('First You tell me!')
let_a=input('Do you Like guesses?😊  ').lower()
if let_a=='yes':
    print('OK! Lets Start it!')
else:
    exit()
import random
guess_range_numbers=random.randint(1,10)
while True:
    let_b=int(input('Enter a number b/w 1 to 10:  '))
    if let_b>guess_range_numbers:
        print('Sorry! Number is Larger!')
    elif let_b<guess_range_numbers:
        print('Sorry! Number is Smaller!')
    elif let_b==guess_range_numbers:
        print('Finally! You got it!😍')
        print('Well don! Great!🤩')
    else:
        print('Invalid number!')

#...................Finished!...............................#
