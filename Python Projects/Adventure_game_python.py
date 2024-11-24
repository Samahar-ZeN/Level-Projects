#.................................Adventure_Game_Python..................................................#


print('Lets Start game!')
print('Before Play this Game! I wanna tell you that this game is about adventure!😁')
print('But Its so funny Game!😄')
let_a=input('Will you like to play this game with me?😊  ').lower()
if let_a=='yes':
    print('OK! Lets Start!')
else:
    exit()
while True:
    print(''''You are walking alone in forest and you see that a lion 🐆 infront of you! 
          There are three ways to escape!
          1) Left
          2) Right
          3) River
          Which one you will be choose?   ''')
    let_b=input('Choose One way!  ').lower()
    if let_b=='left':
        print('There are more lions also!🐆')
    elif let_b=='right':
        print('There,the road was blocked!')
    elif let_b=='river':
        print('Crocodiles are waiting of yours!🐊')
    else:
        print('You will die!')

#...........................Finished!................................#
    