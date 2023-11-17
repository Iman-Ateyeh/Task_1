
class customer_account:
    def __init__(self, username, balance=0): 
        #creating an initial instance of the bank account. 
        self.username = username    
        self.balance = balance
        self.transaction_history = []        

    def display_available_balance(self):
        print(f"{self.username}, your account balance is ${self.balance:.3f}") #display customer`s available balance. 

    def deposit(self, amount): # depositing new balance and checking if it is > 0 
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"{self.username} deposited ${amount:.3f}")
            print(f"Deposited ${amount:.3f} successfully.")
        else:
            print(" Please enter an amount > 0.")

    def withdraw(self, amount): #withdrawing money and checking if there is enough balance and valid amount
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"{self.username} withdrawn ${amount:.3f}")
                print(f"Withdrawn ${amount:.3f} successfully.")
            else:
                print("Insufficient funds in your account balance.")
        else:
            print("Please enter a valid number.")

    def display_transaction_history(self): # displaying all user transactions 
        print(f"\nTransaction History for {self.username}:")
        for transaction in self.transaction_history:
            print(transaction)

def create_account(accounts):
    username = input("Enter your username: ")
    if username in accounts:
        print("Username already exists. Please choose a different one.")
        return None
    password = input("Enter your password: ")
    accounts[username] = {'password': password, 'account': customer_account(username)} # create a new user 
    print(f"Account for {username} created successfully.")
    return accounts[username]['account']

def authenticate(accounts): 
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in accounts and accounts[username]['password'] == password:
        return accounts[username]['account']
    else:
        print("Invalid username or password. Please try again.")
        return None

def main():
    accounts = {}
    current_account = None

    while True:
        print("\n===== Simple Banking System =====")
        print("1. Create Account")
        print("2. Log In")
        print("3. Exit")

        order = input("Enter your order (1-3): ")

        if order == '1':
            current_account = create_account(accounts)
        elif order == '2':
            current_account = authenticate(accounts)
        elif order == '3':
            exit_program()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

        if current_account: # if current account is not none 
            run_account_operations(current_account) 

def get_positive_float_input(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            else:
                print("Invalid input. Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def run_account_operations(account):
    actions = {
        '1': account.display_available_balance,
        '2': lambda: account.deposit(get_positive_float_input("Enter the amount to deposit: ")), # check if the amount is > 0 and display the needed statement. (build-in function)
        '3': lambda: account.withdraw(get_positive_float_input("Enter the amount to withdraw: ")),
        '4': account.display_transaction_history,
        '5': exit_program
    }

    while True:
        print("\n===== Account Operations =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Log Out")

        order = input("Enter your order (1-5): ")

        if order in actions:
            actions[order]()
        else:
            print("Invalid order Please enter a number between 1 and 5.")

def exit_program():
    print("Thank you for using our banking system. Goodbye!")
    exit()

if __name__ == "__main__":
    main()
