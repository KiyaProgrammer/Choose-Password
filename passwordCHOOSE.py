import random
characters='abcdefghigklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#number of characters
print('## Welcome ##')
char=int(input('Enter Number of character : '))
def choosepassword():
    password=''
    for i in range(char):
        choose=random.choice(characters)
        password=choose+password
    print(f'Your password : {password}') 
    Again() 
def Again():
    again=input('do you like password (y=yes,n=no)? : ')
    if again.lower()=='y':
        print('Thanks You')
    elif again.lower()=='n':
        choosepassword()
    else:
        print('Enter Y or N!!!')
        Again() 
choosepassword()
           