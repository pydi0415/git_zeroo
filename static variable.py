# class Employee:
#     comp_name="Sathya"
#     comp_cno=7093963363
# print(Employee.comp_name)
# print(Employee.comp_cno)
class BankAccount:
    def __init__(self):
        self.NameOfTheDepasitor="prabhakar"
        self.AccountNumber=123456789
        self.typeofaccount="savings account"
        self.balance=1000
    # def deposit(self):
    #     amount = 500
    #     self.balance += amount
    #     print("\n Amount Deposited:", amount)

    # def withdraw(self):
    #    amount = 300
    #    if self.balance >= amount:
    #     self.balance -= amount
    #     print("\n You Withdrew:", amount)
    #    else:
    #     print("\n Insufficient balance  ")
    def display(self):
        print("NameOfTheDepasitor:",self.NameOfTheDepasitor)
        print("AccountNumber:",self.AccountNumber)
        print("balance:",self.balance)
s=BankAccount()
# s.deposit()
# s.withdraw()
s.display()






# class savingsAccount:
#
