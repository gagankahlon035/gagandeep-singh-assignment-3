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
    print("****************************************")
    print("          PIXELL RIVER FINANCIAL")
    print("              AIM SIMULATOR")
    print()
    print(f"  your current balance is: ${balance: ,.2f}")
    print()
    print("                 Deposit: D")
    print("                 Withdraw: W")
    print("                 Quit: Q")
    print("****************************************")
    