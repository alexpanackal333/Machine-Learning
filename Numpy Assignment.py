#!/usr/bin/env python
# coding: utf-8

# 1.Write a function so that the columns of the output matrix are powers of the input
# vector.
# The order of the powers is determined by the increasing boolean argument. Specifically, when 
# increasing is False, the i-th output column is the input vector raised element-wise to the power 
# of N - i - 1.
# HINT: Such a matrix with a geometric progression in each row is named for AlexandreTheophile Vandermonde.

# In[1]:


import numpy as np


# In[2]:


a=np.array([1,2,3,4,5])
np.vander(a)


# 2.Write a function to find moving average in an array over a window:
# Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.

# In[3]:



dataset = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]


# In[28]:


a=np.array(dataset)
def moving_avg(data,n):
    avrg_sum = np.cumsum(a, dtype=float)
    avrg_sum[n:] = avrg_sum[n:] - avrg_sum[:-n] 
    return avrg_sum[n - 1:] / n
    
moving_avg(dataset,3)


# In[ ]:




