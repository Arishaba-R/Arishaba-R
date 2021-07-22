#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[ ]:


#Write a function called numbers that takes a parameter called given_number that print fizz if the given_number is a multiple of 3,
#it should print buzz if a number is a multiple of 5
#It should print fizzbuzz if a number is multiple of 3 and 5:


# In[ ]:



def numbers(given_number):
    if given_number %3==0 and given_number %5==0:
        print("FizzBuzz")   
    elif given_number %3==0:
        print("Fizz")
    elif given_number %5==0:
        print("Buzz")
        


# In[ ]:


numbers(15)


# # Question_2

# In[ ]:


#Given two lists; list_a, list_b. Write a function that prints (lists are equal) If list_a is equal to list_b. Else if prints(the two lists are not equal)
#Function name should be called compare_lists which takes two parameters called list_a, and list_b


def compare_lists(list_a, list_b):
    list_a_sorted=sorted(list_a)  
    list_b_sorted=sorted(list_b) 
    if list_a_sorted == list_b_sorted:
        print ( "Lists are equal")
        
    else:
        print( "Lists are not equal")
    


# In[ ]:


compare_lists([1,2,3,5,4,5,6],[1,2,5,7,9])


# In[ ]:


compare_lists([1,2,3,4,5],[1,2,3,4,5])


# # Question_3

# In[ ]:


#Wite a program that takes into parameters word_a, and word_b, which checks if both words are an anagram. It should print word_a, and word_b are an anagram, else print word_a, and word_b, are not an anagram

#Anagrams are words with the same letters: for example Eat, Ate
def Anagram_1( word_a, word_b):
    word_a_sorted =sorted(word_a)
    word_b_sorted =sorted(word_a)
 
    if word_a_sorted == word_b_sorted:
        print("word_a, and word_b are anagrams")
        
    else:
        print("word_a, and word_b are anagrams")


# In[ ]:



Anagram_1("Eat", "Tea")

Anagram_1("Nap", "Pan")


# # Question 4
# 

# In[ ]:


"""
Question 4


Write a program that creates a banking system for a church,high networth people and companies

hints

class bank_Account: Takes in parameters like firstName, lastName, sex, deposited_amount

withdrawl function - How much is available for withdrawal

deposit function - how much was deposited

balance function - What is the balance



class High_networth_individuals: - Inherents for class bank
This class has a secret_key parameter -

def introduction - return or print my name is and my sex is.


class companies:- inherit from bank Acct - has new parameter called company id

def company_introduction - print our company is {name of comapny} and {company id}



Output

create 3 objects to test if your code is working


def __init__(self, put ypur parameters here) - this is the constructor

every fucntion in a class has the self parameter.

"""


# In[23]:


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
    
            


# In[20]:


#Ojects used are A1, A2, A3
A1_1 = Bank_Account("Ritah", "Arishaba", "Female", 1000)
A1_1.withdrawal()
A1_1.deposited()
A1_1.balance()


# In[24]:


#Ojects used are A1, A2, A3
A1_1 = High_networth_individuals("Alpha", "Ngwenya", "Male", 1000, 4408)
A1_1.withdrawal()
A1_1.deposited()
A1_1.balance()
A1_1.Introduction()


# In[ ]:





# In[ ]:




