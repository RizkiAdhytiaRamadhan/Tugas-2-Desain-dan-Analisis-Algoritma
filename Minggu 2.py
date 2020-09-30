#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[7]:


print(np.__version__)


# # III. Big O Onotation
# ## 1. Constant Time (O(1))
# If an algorithm takes the same amount of time to run, independent of the size of the input data, it is said to constant time. it is represented by O(1)

# In[18]:


def getFirst(myList):
    return myList[0]


# In[19]:


getFirst([1,2,3])


# # 2. Linear Time (O(n)) Complexity

# ##  Linear Time (O(n)) Complexity

# An Algorith is said to have a complexity of linear time, represented by O(n), if the execution time is directly proportional to the size of the input.

# In[22]:


def getSum(myList):
    sum = 0
    for item in myList:
        sum = sum+item
    return sum
#Perhatikan posisi spasi pada return


# In[23]:


getSum([1,2,3,4])


# # Quadratic Time(O(n^2)) complexity

# ## Quadratic Time(O(n^2)) complexity

# An algorithm is said to run in quadratic time if the execution time of an alforithm is proportional to the square of the input size

# In[24]:


def getSum(myList):
    sum = 0
    for row in myList:
        for item in row:
            sum += item
    return sum


# In[25]:


getSum([[1,2,5],[3,4,7]])


# # Logarithmic time(O(log(n)) complexity

# ## Logarithmic time(O(log(n)) complexity

# An algorithm is said to run in logarithmic time if the execution time of the algorithm is proportional to the logarithm of the input size

# In[29]:


def searchBinary(myList,item):
    first = 0
    last = len(myList)-1
    foundFlag = False
    while( first<=last and not foundFlag):
        mid = (first+last)//2
        if myList[mid] == item :
            foundFlag = True
        else:
            if item < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return foundFlag


# In[30]:


searchBinary([8,9,10,100,1000,2000,3000], 10)


# In[31]:


searchBinary([6,9,10,100,1000,2000,3000], 5)


# In[ ]:




