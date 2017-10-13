class Bank:

    def __init__(self, name):
        self.name = name
        self.bal = 25000

    def verification(self):
        self.pin = input("Enter your PIN : ")
        if self.pin == "1234":
            print("Hello {}".format(self.name))
            self.menu()
        else:
            print("Wrong PIN")

    def menu(self):
        print("""
        1. Withdraw
        2. Deposit
        3. Balance Enquiry
        4. Quit
        """)

        todo = {
            "1" : self.withdraw,
            "2" : self.deposit,
            "3" : self.balanceEnq,
            "4" : quit
        }

        userChoice = input("Enter your choice : ")

        todo.get(userChoice)()

    def withdraw(self):
        withdrawAmount = int(input("Enter the amount you want to withdraw : "))
        if self.bal < withdrawAmount:
            print("Not enough money in your account...")
            self.menu()
        else:
            self.bal = self.bal - withdrawAmount
            print("Remaining Balance",self.bal)
            self.menu()

    def deposit(self):
        depositAmount = int(input("Enter the amount you want to deposit"))
        self.bal = self.bal + depositAmount
        print("Current Balance",self.bal)
        self.menu()

    def balanceEnq(self):
        print("Available Balance :",self.bal)
        self.menu()

user_1 = Bank("Ram")
user_1.verification()

