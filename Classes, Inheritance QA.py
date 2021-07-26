#!/usr/bin/env python
# coding: utf-8

# """Write a program that creates a banking system for a church,high networth people and companies
# hints
# class bank_Account: Takes in parameters like firstName, lastName, sex, deposited_amount
# withdrawl function - How much is available for withdrawal
# deposit function - how much was deposited
# balance function - What is the balance
# class High_networth_individuals: - Inherents for class bank
# This class has a secret_key parameter -
# def introduction - return or print my name is and my sex is.
# class companies:- inherit from bank Acct - has new parameter called company id
# def company_introduction - print our company is {name of comapny} and {company id}
# Output
# create 3 objects to test if your code is working
# def __init__(self, put ypur parameters here) - this is the constructor
# every fucntion in a class has the self parameter.
# """

# In[3]:


class Bank_Account:
    def __init__(self, firstName, lastName, sex, deposited_amount):
        self.firstName= firstName 
        self.lastName= lastName
        self.sex= sex
        self.deposited_amount= deposited_amount
        
    def withdrawal(self):
        if self.deposited_amount > 0:
            print(f" {self.deposited_amount} is available for withdrawal")
        else:
            print("There is no available for withdrawal")
    
    def deposited(self):
        if self.deposited_amount > 0:
            print(f" {self.deposited_amount} was deposited into your account")
        else:
            print(f" {self.deposited_amount} is available in your account")
        
    def balance(self):
        if self.deposited_amount > 0:
            print(f" {self.deposited_amount} is the available balance in your account")
        else:
            print("You have insufficient balance in your account")
        

class High_networth_individuals(Bank_Account):
    def __init__(self, firstName, lastName, sex, deposited_amount, secret_key):
            self.secret_key = secret_key
            super().__init__(firstName, lastName, sex, deposited_amount)
            
    def Introduction(self):
        print(f"My name is {self.firstName}, and I am a {self.sex}")
        
        
class companies(Bank_Account):
    def __init__(self, firstName, lastName, sex, deposited_amount, company_id):
            self.company_id = company_id
            super().__init__(firstName, lastName, sex, deposited_amount)
            
    def company_introduction(self):
        print(f"Our company is {self.firstName}, and the {self.company_id} identification number")


# In[4]:


#Ojects used are A1, A2, A3
A1_1 = Bank_Account("Ritah", "Arishaba", "Female", 1000)
A1_1.withdrawal()
A1_1.deposited()
A1_1.balance()


# In[ ]:




