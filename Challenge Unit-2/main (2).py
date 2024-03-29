class BankAccount:
  def __init__(self, account_number, account_holder_name,initial_balance=0.0):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = initial_balance
    
  def deposit(self,amount):
      if amount > 0:
          self.__account_balance +=amount
          print("Deposited ₹{}.New balance: ${}".format(amount,self.__account_balance)) 
      else:  
          print("Invalid deposit amount.")
  def withdraw(self, amount):
      if(amount > 0)and(amount <=                self.__account_balance):
         self.__account_balance -= amount
         print("withdraw ₹{}. New balance: ₹{}".format(amount,        self.__account_balance))
      else:
         print("Invalid withdraw amount             or insufficient balance.")
  def display_balance(self):
         print("Account balance for {}       (Account#{}): ₹{}".format(
                self.__account_holder_name, self.__account_number,
                self.__account_balance))
myaccount = BankAccount(account_number = "817182331",
    account_holder_name="Sobiyarp8", 
    initial_balance=5000) 
myaccount.display_balance()
myaccount.deposit(500)
myaccount.withdraw(20000)
myaccount.display_balance()
