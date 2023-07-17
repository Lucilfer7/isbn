import pyperclip as pc
import os

os.system('cls')

while True:
    try:
        userInput = input(f"\x1b[3m\x1b[1;35mEnter the ISBN: \x1b[0m\x1b[3;34m")
        dashRemoved = userInput.replace("-", "")
        isbn = int(dashRemoved)
        if isbn == 0:
            break
        print(f'\x1b[1;32m{isbn}')
        pc.copy(isbn)
    except:
        print(f"\x1b[1;31mInvalid data")

os.system('cls')