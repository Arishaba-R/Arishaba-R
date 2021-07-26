#!/usr/bin/env python
# coding: utf-8

# # Comparing Lists

# In[1]:


def compare_lists(list_a, list_b):
    list_a_sorted=sorted(list_a)  
    list_b_sorted=sorted(list_b) 
    if list_a_sorted == list_b_sorted:
        print ( "Lists are equal")
        
    else:
        print( "Lists are not equal")


# In[ ]:




