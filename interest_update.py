import csv
from pprint import pprint

account_balance = {}

with open("account_balance.txt", "r") as file:
    for line in file:
        account_number, balance = line.strip().split("|")
        account_balance[account_number] = float(balance)

pprint("Initial Account Balances: ")
pprint(account_balance)

