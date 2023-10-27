class Account:
    def __init__(self, name, email, password, address, account_type) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.account_type = account_type
        self.account_num = str(len(self.name)) + str(len(self.email))
        self.__balance = 0
        self.transaction_hitory = []
        self.loan_limit = 2
        self.loan_enabled = True
        self.is_bankrupt = False

    def __repr__(self) -> str:
        return f"Name: {self.name} Address: {self.address} Email: {self.email} Account Type {self.account_type}"

    def deposite(self, amount: int):
        self.__balance += amount
        self.transaction_hitory.append({
            "Type": "Deposite",
            "Amount": amount,
        })
        print(f"\n\tSuccessfully deposite {amount} BDT")

    def withdraw(self, amount: int):
        if self.is_bankrupt is False:
            if self.__balance > amount:
                self.__balance -= amount
                self.transaction_hitory.append({
                    "Type": "Withdraw",
                    "Amount": amount
                })
                print(f"\n\tSuccessfully Withdraw: Amount {amount}")
            else:
                print("Withdrawal amount exceeded")
        else:
            print("You're Bunkrupt")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance += value

    def check_history(self):
        for history in self.transaction_hitory:
            print("------Transaction History-------")
            for key, value in history.items():
                print(key, value)
