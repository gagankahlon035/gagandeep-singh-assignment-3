import csv
from pprint import pprint

account_balances = {}

with open("account_balances.txt", "r") as file:
    for line in file:
        account_number, balance = line.strip().split("|")
        account_balances[account_number] = float(balance)

print("Initial Account Balances: ")
pprint(account_balances)

for account_number, balance in account_balances.items():
    if balance < 0:
        rate = 0.10
    elif balance < 1000:
        rate = 0.01
    elif balance < 5000:
        rate = 0.025
    elif balance >= 5000:
        rate = 0.05

    interest_earned = (balance * rate) / 12
    account_balances[account_number] +=interest_earned

print("updated Account Balances after interest: ")
pprint(account_balances)

csv_filename = "updated_balances_GS.csv"

with open(csv_filename, "w", newline= "") as file:
    file.write("Account, Balance\n")
    for account_number, balance in account_balances.items():
        file.write(f"{account_number}, {balance}\n")

print(" Final Data from the CVS file: ")
with open (csv_filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

## Add review
