# 4. BANKING OPERATIONS

def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
    else:
        print("Invalid deposit amount.")
    return balance


def withdraw(balance, amount):
    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
    return balance


def check_balance(balance):
    return balance


def display_account(name, balance):
    print("\n----- BANK ACCOUNT -----")
    print("Account Holder:", name)
    print(f"Balance: ₹{balance:.2f}")


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: ₹"))

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: ₹"))
        balance = deposit(balance, amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: ₹"))
        balance = withdraw(balance, amount)

    elif choice == "3":
        print(f"Current Balance: ₹{check_balance(balance):.2f}")

    elif choice == "4":
        display_account(name, balance)
        print("Thank you for using banking services.")
        break

    else:
        print("Invalid choice.")