#..................................Quiz Python Project.....................................#


print('Lets Start Quiz Game!!!🥰')
print('Its so funny game...😄')
let_take_input=input('Do you want to play quiz game with me?  ').lower()
if let_take_input=='yes':
    print('OK! Lets Start!🤩')
else:
    exit()
score=0
while True:
    print('Question # 1:')
    a=input('Which country drinks the most coffee per capita?  ').lower()
    if a=='finland':
        print('Correct! Well done!🥰')
        score+=1
    else:
        print('Wrong!☹')
    print('Question # 2:')
    b= input('Cacio e pepe is a staple of what Italian city’s cuisine?  ').lower()
    if b=='rome':
        print('Correct! Well done!🥰')
        score+=1
    else:
        print('Wrong!☹')
    print('Question # 3:')
    c=input('Where did sushi originate?  ').lower()
    if c=='japan':
        print('Correct! Well done!🥰')
        score+=1
    else:
        print('Wrong!☹')
    print('Question # 4:')
    d=input('What meat is used in a shepherds pie?  ').lower()
    if d=='lamb':
        print('Correct! Well done!🥰')
        score+=1
    else:
        print('Wrong!☹')
    print('Question # 5:')
    e=input('Which country is credited with inventing ice cream?   ').lower()
    if e=='china':
        print('Correct! Well done!🥰')
        score+=1
    else:
        print('Wrong!☹') 
    print(f'Your score is:{score/5 *100} %')
    print('Congratulations! Well Played!🤩🤩')


#..................Finished!...........................#