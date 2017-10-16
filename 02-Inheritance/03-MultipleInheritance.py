class Emp:

    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0
        self.company = "HCL"

    def printEmp(self):
        print("Emp Details :",self.name, self.age, self.salary, self.company)


class Bank:

    def __init__(self,balance,eligible):
        self.balance = balance
        self.eligible = eligible
        self.bank = "HDFC"

    def checkEligibility(self):
        print("Welcome to {} bank".format(self.bank))
        if self.eligible:
            print("Your balance is {} You will get the loan".format(self.balance))
        else:
            print("You are not eligible because your balance is {}".format(self.balance))


class Emp_1(Emp, Bank):

    def __init__(self, name,age,salary):
        Emp.__init__(self)
        self.name = name
        self.age = age
        self.salary = salary

    def checkBalance(self):

        if self.salary > 15000:
            self.eligible = True
            Bank.__init__(self, self.salary, self.eligible)
        else:
            self.eligible = False
            Bank.__init__(self, self.salary, self.eligible)


ram = Emp_1("Ram", 20,19000)
ram.printEmp()
ram.checkBalance()
ram.checkEligibility()
