"""This project contain an ATM simulator where users can deposit and 
withdraw money"""

__author__ = "Gagandeep Singh"
__version__ = "1.0.0"

import random
import os
from time import sleep

menu_options = {"D": "Deposit", "W" : "withdraw","Q" : "Quit"}

balance = random.randint(-1000, 10000)

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("*" * 40)
    print("PIXELL RIVER FINANCIAL".center(40))
    print("ATM Simulator".center(40))
    print()
    print(f"Your current balance is: ${balance: ,.2f}". center(40))
    print()
    print("Deposit: D".center(40))
    print("Withdraw: W".center(40))
    print("Quit: Q".center(40))
    print("*" * 40)

    selection = input("Enter your selection: ").strip().upper()

    if selection not in ["D","W","Q"]:
        print()
        print("*" * 40)
        print("INVALID SELECTION".center(40))
        print("*" * 40)
        sleep(3)
        continue

    elif selection == "Q":
        break
    amount = float(input("Enter your transaction amount: "))
    if selection == "D":
        balance += amount
    elif selection == "W":
        if amount > balance:
            print()
            print("*" * 40)
            print("INSUFFICIENT FUNDS".center(40))
            print("*" * 40)
        else:
            balance -= amount

    print()
    print("*" * 40)
    print(f"Your current balance is: ${balance: ,.2f}".center(40))
    print("*" * 40)
    sleep(3)
    os.system("cls" if os.name == "nt" else "clear")

                