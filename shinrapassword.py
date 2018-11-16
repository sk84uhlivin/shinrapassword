#!/usr/bin/python3

programRunning = True

passwords = ["MAKO (5)", "KING (2)", "BEST (1)", "BOMB (4)"]

commands = ["list", "quit"]

def passList():
    print()
    for x in range(20):
        print(
            "{:<02d} {} | {:<02d} {} | {:<02d} {}".format(
                x,
                passwords[x % 4],
                x + 20,
                passwords[(x + 20) % 4],
                x + 40,
                passwords[(x + 40) % 4],
            )
        )
while programRunning:              
    print()
    cmd = input("Type the in-game second, 'list' or 'quit'. ").lower()
    try:
        cmd = int(cmd) % 4

    except ValueError:
        if cmd not in commands:
            print()
            print('Invalid command.')
            continue

    if cmd == 'list':
        passList()

    elif cmd == 'quit':
        programRunning = False
        break 

    else:
        print()
        print("The password is {}".format(passwords[cmd]) + ".")

    
