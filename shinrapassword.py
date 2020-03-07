#!/usr/bin/env python3

passwords = ["MAKO (5)", "KING (2)", "BEST (1)", "BOMB (4)"]

commands = ["list", "quit", "l", "q"]

def passList():
    print()
    for x in range(20):
        print(
            "{:02d} {} | {:<02d} {} | {:<02d} {}".format(
                x,
                passwords[x % 4],
                x + 20,
                passwords[(x + 20) % 4],
                x + 40,
                passwords[(x + 40) % 4],
            )
        )
while True:              
    print()
    cmd = input("Type the in-game second, '(l)ist' or '(q)uit'. ").lower()

    try:
        modulo = int(cmd) % 4

    except ValueError:
        if cmd not in commands:
            print()
            print('Invalid command.')
            continue

    if cmd in ('list', 'l'):
        passList()

    elif cmd in ('quit', 'q'):
        print()
        break 

    else:
        print()
        print(f"The password is {passwords[modulo]}.")

    
