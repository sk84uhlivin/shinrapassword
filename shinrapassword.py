#!/usr/bin/python3

programRunning = True

def passList():
    x = 0
    print()
    while x < 60:
        if x%4 == 0:
            print(str(x).zfill(2),'MAKO')
        elif x%4 == 1:
            print(str(x).zfill(2),'KING')
        elif x%4 == 2:
            print(str(x).zfill(2),'BEST')
        elif x%4 == 3:
            print(str(x).zfill(2),'BOMB')
        x+=1

while programRunning:
    try:
        while programRunning:

            print()
            second = input("Type the in-game second, 'list' or 'quit'. ").lower()

            if second == 'list':
                passList()

            elif second == 'quit':
                programRunning = False
                break 

            elif int(second)%4 == 0:
                print()
                print('The password is MAKO (5).')

            elif int(second)%4 == 1:
                print()
                print('The password is KING (2).')       

            elif int(second)%4 == 2:
                print()
                print('The password is BEST (1).')
               
            elif int(second)%4 == 3:
                print()
                print('The password is BOMB (4).')

    except:
        print()
        print('Invalid command.')
