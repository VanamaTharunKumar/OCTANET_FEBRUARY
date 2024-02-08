class BankAccount:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def display_balance(self):
        print(f"Your balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            self.transactions.append(f"Transfer to {recipient.user_id}: -${amount}")
        else:
            print("Insufficient funds!")

    def display_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

def authenticate_user(accounts):
    user_id = input("Enter your user ID: ")
    pin = input("Enter your PIN: ")

    for account in accounts:
        if account.user_id == user_id and account.pin == pin:
            return account

    return None

def main():
    accounts = [BankAccount("7396", "1421"), BankAccount("9666", "4937")]

    user_account = authenticate_user(accounts)

    if user_account:
        print("Authentication successful. Welcome to the ATM!")
        while True:
            print("\nChoose an option:")
            print("1. Display Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Display Transactions")
            print("6. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                user_account.display_balance()
            elif choice == '2':
                amount = float(input("Enter the deposit amount: $"))
                user_account.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter the withdrawal amount: $"))
                user_account.withdraw(amount)
            elif choice == '4':
                recipient_id = input("Enter the recipient's user ID: ")
                recipient = next((acc for acc in accounts if acc.user_id == recipient_id), None)
                if recipient:
                    amount = float(input("Enter the transfer amount: $"))
                    user_account.transfer(recipient, amount)
                else:
                    print("Recipient not found.")
            elif choice == '5':
                user_account.display_transactions()
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Authentication failed. Please check your user ID and PIN.")

if __name__ == "__main__":
    main()
