class Bank:
    accno:int
    balance:float
    acc_type:str
    cust_name:str
    
    def __init__(self,accno,balance,acc_type,cust_name):
        self.accno=accno
        self.balance=balance
        self.acc_type=acc_type
        self.cust_name=cust_name
        
    def deposit(self,amount):
        
        self.balance+=amount
        
        print(f" your account {self.accno} is credicted with amount {amount}, avl balance -> {self.balance}")
        
    def withdraw(self,amount):
             
        if self.balance<amount:
            print("Insufficient balance..")
        else:
            self.balance-=amount
            print(self.balance)
            
    def get_balance(self):
        print("Available balance is :",self.balance)
        
    
user_1=Bank(497001,12000,"Savings","Sebin")
user_1.deposit(1000)
user_1.withdraw(1000000)
user_1.withdraw(2000)
user_1.get_balance()