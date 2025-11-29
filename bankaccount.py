#need updating balance
#Raise a ValueError if:
#Withdrawal amount is more than balance
#Any amount is negative
#Wrap calls in try/except blocks when testing.

#created custom exception 
class BadWithdrawal(Exception):#inherits from built in exception class
    '''exception raise for withdraw amount bigger than balance'''
    
    def __init__(self,message):
        self.message = message
        
    def __str__(self):
        return f"Withdrawal amount cannot be more than your balance. \nYour withdrawal was unsuccessful."



class BankAccount:
    #class object attribute?
    
    
    def __init__(self,owner,balance):
       
        self.balance = balance
        self.owner = owner
        
    #deposit
    def deposit(self):
        amount = float(input("Deposit Amount: "))
        if amount < 0:
                raise ValueError('amount cannot be negative')
        try:
            self.balance += amount
        except TypeError:
            print('Amount must be a positive number. \nYour deposit was unsuccessful.')
        except:
            print('An error has occurred. \nYour deposit was unsuccessful.')
        else:
            print(f'deposit of ${amount} successful')
            return self.balance

    #withdraw
    def withdraw(self):
        amount = float(input("Withdrawal Amount: "))
        if amount < 0:
                raise ValueError('amount cannot be negative. \nYour Withdrawal was unsuccessful.')
        if amount > self.balance:
            raise BadWithdrawal("Withdrawal amount cannot be more than your balance. \nYour withdrawal was unsuccessful.")
        try:
            self.balance -= amount
        except:
            print('An error has occurred. \nYour withdrawal was unsuccessful.')
        else:
            print(f'withdrawal of ${amount} successful')
            return self.balance
    
    #check balance
    def check_bal(self):
        print(f"Balance: ${self.balance}")

ba1 = BankAccount("Bob",5000)


ba1.deposit()
ba1.check_bal()

            
        
        
            
    