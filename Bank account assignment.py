class Account:
    def _init_(self, id, balance = 0):
        self.id = id
        self.balance = balance

    def getid(self):
        return self.id

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

def main():
    global accounts
    accounts = []
    for x in range(1000, 9999):
        account = Account(x, 25000)
        accounts.append(Account)

main()
    
while True:
    id = int(input("Enter your account PIN: "))

    while id < 1000 or id > 9999:
        id = input("This is an invalid ID, please enter a valid ID.")

    while True:
        print("A - View balance  B - Deposit  C - Withdraw  D - Exit")
        selection = input("Please enter your chosen option.")

        for acc in accounts:
            if acc.getid() == id:
                accountObj = acc
                break

        if selection == 1:
            view_balance = accountObj.getBalance()
            print("Current balance is: ", view_balance)

        elif selection == 2:
            amount = float(input("Enter desired amount to deposit: "))
            ver_deposit = input("Is this the right amount? ")

            if ver_deposit == "Yes":
                print("Verify deposit.")

            if amount < accountObj.getbalance():
                accountObj.deposit(amt)
                print("Deposit successful! New balance is: " + str(accountObj.getbalance))

            else:
                break

        elif selection == 3:
            amount = float(int("Enter desired amount to withdraw: "))
            ver_withraw = input("Is this the right amount? ")

            if ver_withraw == "Yes":
                print("Verify withdraw.")

            if amount < accountObj.getbalance():
                accountObj.withdraw(amt)
                print("Withdraw successful! New balance is: " + str(accountObj.getbalance))

            else:
                print("Balance is less than chosen amount to withdraw.")
                print("Please deposit money or enter a reduced amount.")
            


























