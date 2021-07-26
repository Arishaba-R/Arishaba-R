#!/usr/bin/env python
# coding: utf-8

# # #Write a function called numbers that takes a parameter called given_number that print fizz if the given_number is a multiple of 3; it should print buzz if a number is a multiple of 5; It should print fizzbuzz if a number is multiple of 3 and 5:

# In[ ]:


def numbers(given_number):
    if given_number %3==0 and given_number %5==0:
        print("FizzBuzz")   
    elif given_number %3==0:
        print("Fizz")
    elif given_number %5==0:
        print("Buzz")

