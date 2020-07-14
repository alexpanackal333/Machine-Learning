#!/usr/bin/env python
# coding: utf-8

# It happens all the time: someone gives you data containing malformed strings, 
# Python, lists and missing data. How do you tidy it up so you can get on with the 
# analysis?
# Take this monstrosity as the DataFrame to use in the following puzzles:
# df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 
# 'londON_StockhOlm',
# 'Budapest_PaRis', 'Brussels_londOn'],
# 'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
# 'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
# 'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
# '12. Air France', '"Swiss Air"']})
# 1. Some values in the the FlightNumber column are missing. These numbers are 
# meant to increase by 10 with each row so 10055 and 10075 need to be put in 
# place. Fill in these missing numbers and make the column an integer column 
# (instead of a float column).
# 2. The From_To column would be better as two separate columns! Split each 
# string on the underscore delimiter _ to give a new temporary DataFrame with 
# the correct values. Assign the correct column names to this temporary 
# DataFrame.
# 3. Notice how the capitalisation of the city names is all mixed up in this 
# temporary DataFrame. Standardise the strings so that only the first letter is 
# uppercase (e.g. "londON" should become "London".)
# 4. Delete the From_To column from df and attach the temporary DataFrame 
# from the previous questions.
# 5. In the RecentDelays column, the values have been entered into the 
# DataFrame as a list. We would like each first value in its own column, each 
# second value in its own column, and so on. If there isn't an Nth value, the value 
# should be NaN.
# Expand the Series of lists into a DataFrame named delays, rename the columns 
# delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df 
# with delays.

# 1.Some values in the the FlightNumber column are missing. These numbers are meant to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in these missing numbers and make the column an integer column (instead of a float column).

# In[156]:


import numpy as np
import pandas as pd
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'], 'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]], 'Airline': ['KLM(!)', ' (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})


# In[157]:


df['FlightNumber'].fillna(0,inplace=True)


# In[158]:


df


# In[159]:


for i in range(1,len(df)):
    if df['FlightNumber'].iloc[i] == 0:
        df['FlightNumber'].iloc[i]=df['FlightNumber'].iloc[i-1]+10


# In[160]:


df['FlightNumber']


# In[161]:


df


# In[162]:


df['FlightNumber'] = df['FlightNumber'].astype('int64')


# In[163]:


df.dtypes


# 2.The From_To column would be better as two separate columns! Split each string on the underscore delimiter _ to give a new temporary DataFrame with the correct values. Assign the correct column names to this temporary DataFrame.

# In[164]:


From_list=[]
To_list=[]
split_list=[]
for i in df['From_To']:
    split_list=i.split('_')
    From_list.append(split_list[0])
    To_list.append(split_list[1])
print(From_list)
print(To_list)


# In[165]:



df1=pd.DataFrame({'From':From_list,"To":To_list})


# In[166]:


df1


# 3.Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame. Standardise the strings so that only the first letter is uppercase (e.g. "londON" should become "London".)

# In[167]:


df1['From']=df1['From'].str.capitalize()
df1['To']=df1['To'].str.capitalize()


# In[168]:


df1


# 4.Delete the From_To column from df and attach the temporary DataFrame from the previous questions.

# In[169]:


df.drop('From_To',axis=1,inplace=True)


# In[170]:


df


# In[171]:


df=df1.join(df)


# In[172]:


df


# 5.In the RecentDelays column, the values have been entered into the DataFrame as a list. We would like each first value in its own column, each second value in its own column, and so on. If there isn't an Nth value, the value should be NaN. Expand the Series of lists into a DataFrame named delays, rename the columns delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df with delays.

# In[ ]:





# In[177]:


delays = df['RecentDelays'].apply(pd.Series)
delays
delays.columns = ['delay_{}'.format(n) for n in range(1, len(delays.columns)+1)]
delays.columns
df = df.drop('RecentDelays', axis=1).join(delays)
df
    


# In[ ]:




