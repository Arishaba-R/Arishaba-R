#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Transpose a matrix 


def transpose_mat(matrix):
    
    #My target result
    result = [[0,0,0],
         [0,0,0]]

    #Itarate over the rows
    for i in range(len(matrix)):
        #Itarate over the columns
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
        
    for r in result:
        print(r)


# In[12]:


transpose_mat( [[1,2],[3,4],[5,6]])


# In[4]:


a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

ans = ([[x, y, z] for x in a for y in b for z in c])
        
print(ans)


# In[ ]:




