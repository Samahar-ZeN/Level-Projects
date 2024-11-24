#....................................(R,P,S) Game_Python.............................#


print('Lets Start Game!')
print('This game is so funny and amazing!😍 Because its our childhood Game!😅')
let_a=input('Will you like to play with me?🥰  ').lower()
if let_a=='yes':
    print('OK! Then,Lets Start!')
else:
    exit()
ch=('r','p','s')
emojis={'r':'🗿','p':'📄','s':'✂'}
import random
while True:
    let_b=input('Choose one:(r,p,s): ').lower()
    comp_choice=random.choice(ch)
    print(f'You choose {emojis[let_b]}')
    print(f'Computer choose {emojis[comp_choice]}')
    if let_b==comp_choice:
        print('Tie!✋')
    elif let_b=='r'and comp_choice=='s':
        print('You Win!🤩')
    elif let_b=='s' and comp_choice=='p':
         print('You Win!🤩')
    elif let_b=='p' and comp_choice=='r':
         print('You Win!🤩')
    else:
        print('You lose!👎')


#................Finished!........................#