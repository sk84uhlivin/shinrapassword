#!/usr/bin/python3

programRunning = True

x = 0

while programRunning:

    print()
    second = input("What is the in-game second? Type 'quit' or 'list'. ")

    

    if second == 'list':
        while x < 61:
            if x%4 == 0:
                print(x,'MAKO')
            elif x%4 == 1:
                print(x,'KING')
            elif x%4 == 2:
                print(x,'BEST')
            elif x%4 == 3:
                print(x,'BOMB')
            x+=1

    elif second == 'quit':
        programRunning = False
        break 

    elif int(second)%4 == 0:
        print('The password is MAKO (5).')

    elif int(second)%4 == 1:
        print('The password is KING (2).')       

    elif int(second)%4 == 2:
        print('The password is BEST (1).')
       
    elif int(second)%4 == 3:
        print('The password is BOMB (4).')
