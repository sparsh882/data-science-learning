class ATM:

    def __init__(self):
        self.pin = None
        self.balance = 0
        self.run()

    def run(self):
        while True:
            self.menu()

    def menu(self):
        user_input = input("""
Welcome to ATM System
1. Create PIN
2. Change PIN
3. Check Balance
4. Withdraw Money
5. Exit
Enter your choice: """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        elif user_input == '5':
            print("Thank you for using the ATM. Goodbye!")
            exit()
        else:
            print("Invalid option. Please try again.")

    def create_pin(self):
        if self.pin is not None:
            print("PIN already exists. You can change it instead.")
            return

        self.pin = input("Set your new PIN: ")
        try:
            self.balance = int(input("Enter initial balance: "))
            print("PIN created successfully.")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def change_pin(self):
        old_pin = input("Enter your current PIN: ")

        if old_pin == self.pin:
            new_pin = input("Enter your new PIN: ")
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect PIN. Access denied.")

    def check_balance(self):
        user_pin = input("Enter your PIN: ")

        if user_pin == self.pin:
            print(f"Your current balance is: {self.balance}")
        else:
            print("Incorrect PIN. Cannot display balance.")

    def withdraw(self):
        user_pin = input("Enter your PIN: ")

        if user_pin == self.pin:
            try:
                amount = int(input("Enter withdrawal amount: "))
                if amount <= 0:
                    print("Amount must be greater than zero.")
                elif amount <= self.balance:
                    self.balance -= amount
                    print(f"Withdrawal successful. Remaining balance: {self.balance}")
                else:
                    print("Insufficient balance.")
            except ValueError:
                print("Invalid amount entered.")
        else:
            print("Incorrect PIN. Transaction denied.")


# this is object of atm class that i made 
atm = ATM()
