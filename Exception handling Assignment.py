#!/usr/bin/env python
# coding: utf-8

# #  Exception handling Assignment

# 1. Write a function to compute 5/0 and use try/except to catch the exceptions.

# In[1]:


def division(a,b):
    try:
        c=a/b
        return c
    except ZeroDivisionError:
        print("can't divide by zero")
    except:
        print("Error")


division(5,0)


# 2. Implement a Python program to generate all sentences where subject is in
# ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
# ["Baseball","cricket"].
# Hint: Subject,Verb and Object should be declared in the program as shown below.
# subjects=["Americans ","Indians"]
# verbs=["play","watch"]
# objects=["Baseball","Cricket"]
# Output should come as below:
# Americans play Baseball.
# Americans play Cricket.
# Americans watch Baseball.
# Americans watch Cricket.
# Indians play Baseball.
# Indians play Cricket.
# Indians watch Baseball.
# Indians watch Cricket.

# In[2]:


subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

for i in subjects:
    for j in verbs:
        for k in objects:
            print(i+" "+j+" "+k)


# In[ ]:




