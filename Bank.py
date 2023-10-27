from Account import Account


class Bank:
    def __init__(self) -> None:
        self.__bank_amount = 0
        self.__loan_amount = 0
        self.users = []

    def creat_account(self, name, email, password, address, account_type):
        account = Account(name, email, password, address, account_type)
        self.users.append(account)
        return account

    def add_account(self,account):
        self.users.append(account)

    def delete_account(self, account_num):
        for user in self.users:
            if account_num in user.account_num:
                self.users.remove(user)
                print("\n\tAccount Deleted Successfully!")
            else:
                print("\n\tEntered Account Number is Invalid")

    def see_all_accounts(self):
        for user in self.users:
            print(user)

    def bank_balance(self):
        for user in self.users:
            self.__bank_amount+= user.balance
        return self.__bank_amount

    def check_loan_amount(self):
        print(self.__loan_amount)

    def chage_laon_feature(self, account_num):
        for user in self.users:
            if account_num in user.account_num:
                print("\n\tPress 'y' to on loan feature\nPress 'n' to off loan feature")
                op = input("\n\tEnter Option: ")
                if op == 'y':
                    user.loan_enabled = True
                elif op == 'n':
                    user.loan_enabled = False
                else:
                    print("\n\tInvalid Option")
            else:
                print("\n\tEntered Account Number is Invalid")

    def find_account(self, email, password):
        for user in self.users:
            if email in user.email and password in user.password:
                return user

    def money_transfer(self, to_account_num, from_account_num, amount):
        flag = False
        for user in self.users:
            if from_account_num in user.account_num:
                if user.balance > amount:
                    for user2 in self.users:
                        if to_account_num in user2.account_num:
                            user2.balance = amount
                            user2.transaction_hitory.append({
                                "Type": "Cash In",
                                "Amount": amount
                            })
                            user.withdraw(amount)
                            flag = True
                            return
                else:
                    print(
                        f"\n\tEntered amount is greater then you blance\nYour Blance is{user.balance}")
                    return
        if flag is False:
            print("\n\tEntered Account Number is Invalid")

    def take_loan(self, account_num, amount):
        flag = False
        for user in self.users:
            if account_num in user.account_num:
                if user.loan_enabled is True:
                    if user.loan_limit > 0:
                        user.balance = amount
                        user.transaction_hitory.append({
                            "Type": "Bank Loan",
                            "Amount": amount
                        })
                        self.__loan_amount += amount
                        self.__bank_amount-=amount
                        user.loan_limit -= 1
                        print("\n\tLoan amount Successfully Added to your Acount")
                        flag = True
                        return
                    else:
                        print("You already take loan two times")
                        return
                else:
                    print("Your loan feature is off")
                    return
        if flag is False:
            print("Entered Account Number is Invalid")


admin = Account("admin", "admin@gmail.com", "123", "dhaka", "savings")
dbl = Bank()
dbl.users.append(admin)
crntUser = admin

while True:
    if crntUser == None:
        print("\n\t--->!!! No logged in user\n")
        opt = input("Log in or Registration (L/R): ")
        if opt == 'L':
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            crntUser = dbl.find_account(email, password)
        elif opt == 'R':
            name = input("Enter Account Holder name: ")
            email = input("Enter Accound Holder Email: ")
            password = input("Enter Password: ")
            address = input("Enter Address: ")
            account_type = input("Enter Accounty type: ")
            user = dbl.creat_account(
                name, email, password, address, account_type)
            print(f"\n\tYour Account Number is:{user.account_num}")
            crntUser = user
        else:
            print("Invalid Option")
            break
    elif crntUser.name == 'admin' and crntUser.password == "123":
        print("--------Hello Admin-------------")
        print("Options:\n")
        print("1: Create an Account:")
        print("2: Delete user account:")
        print("3: See all acounts list:")
        print("4: Check Total Balance of the Bank:")
        print("5: Check Total loan amount:")
        print("6: Modify Loan Feature:")
        print("7: Log out:")
        choice = int(input("Enter Option: "))
        if choice == 1:
            print("Creating a Account Give the following infromtion")
            name = input("Enter Account Holder name: ")
            email = input("Enter Accound Holder Email: ")
            password = input("Enter Password: ")
            address = input("Enter Address: ")
            account_type = input("Enter Accounty type: ")
            user = dbl.creat_account(
                name, email, password, address, account_type)
            print(
                f"Account Created Successfully-> {user.account_num} Account Number")
        elif choice == 2:
            print("Give Account Number for deleting Account")
            account_num = input("Enter Account Number: ")
            dbl.delete_account(account_num)
        elif choice == 3:
            dbl.see_all_accounts()
        elif choice == 4:
           print(f"\nTotal Blance of the Bank {dbl.bank_balance()}")
        elif choice == 5:
            dbl.check_loan_amount()
        elif choice == 6:
            account_num = input("Enter Account Number: ")
            dbl.chage_laon_feature(account_num)
        elif choice == 7:
            crntUser = None
        else:
            print("Invalid Option")
    elif crntUser:
        print("\n------------------------------------")
        print(f"\tWelcome {crntUser.name} !")
        print("-------------------------------------")
        print("Options:\n")
        print("1: Deposite on you Account: ")
        print("2: Witdraw from you Account: ")
        print("3: Check Available Blance: ")
        print("4: Takle loan from Bank: ")
        print("5: Check Transection History: ")
        print("6: Sendmoney to Another Account: ")
        print("7: Logout: ")
        opt = int(input("Enter Option: "))
        if opt == 1:
            amount = int(input("Enter Deposite Amount: "))
            crntUser.deposite(amount)
        elif opt == 2:
            amount = int(input("Enter Withdrawal Amount: "))
            crntUser.withdraw(amount)
        elif opt == 3:
            print(f"\nYour Current Balance is {crntUser.balance}")
        elif opt == 4:
            account_num = input("Enter Account Number: ")
            amount = int(input("Enter Amount: "))
            dbl.take_loan(account_num, amount)
        elif opt == 5:
            crntUser.check_history()
        elif opt == 6:
            account_num = input("Enter Sender Acount Number: ")
            amount = int(input("Enter Amount: "))
            dbl.money_transfer(account_num, crntUser.account_num, amount)
        elif opt == 7:
            crntUser = None
        else:
            print("Invalid Option")
