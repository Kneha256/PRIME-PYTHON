#wrapping data + methods in a single class
#use to achive data hidding
#Access modifiers - public(by default), private(access within same class), protected(access by class and subclass)
#we use getter and setter for accessing private and protected datas

class BankAccount:
    def __init__(self, name, balance):
        self.name = name     #public
        self.__balance = balance   #private-data mangling

    def get_balance(self):    #getter
            return self.__balance
    
    def set_balance(self, newBalance):   #setter
         self.__balance=newBalance

a1=BankAccount("neha", 17000)
a1.set_balance(21000)
print(a1.name, a1.get_balance())
print(a1._BankAccount__balance)   #to access private attributes with getter