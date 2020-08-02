#!/usr/bin/env python
# coding: utf-8

# 1.Scipy:
# We have the min and max temperatures in a city In India for each months of the year.
# We would like to find a function to describe this and show it graphically, the dataset
# given below.
# Task:
# 1.fitting it to the periodic function
# 2.plot the fit
# Data
# Max = 39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25
# Min = 21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize


# In[3]:


temp_max = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
temp_min = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])

import matplotlib.pyplot as plt
months = np.arange(12)
plt.plot(months, temp_max, 'ro')
plt.plot(months, temp_min, 'bo')
plt.xlabel('Month')
plt.ylabel('Min and max temperature')


# In[5]:


def yearly_temps(times, avg, ampl, time_offset):
    return (avg
            + ampl * np.cos((times + time_offset) * 2 * np.pi / times.max()))

res_max, cov_max = optimize.curve_fit(yearly_temps, months,
                                      temp_max, [20, 10, 0])
res_min, cov_min = optimize.curve_fit(yearly_temps, months,
                                      temp_min, [-40, 20, 0])


# In[6]:


days = np.linspace(0, 12, num=365)

plt.figure()
plt.plot(months, temp_max, 'ro')
plt.plot(days, yearly_temps(days, *res_max), 'r-')
plt.plot(months, temp_min, 'bo')
plt.plot(days, yearly_temps(days, *res_min), 'b-')
plt.xlabel('Month')
plt.ylabel('Temperature ($^\circ$C)')

plt.show()


# In[ ]:





# 2.Matplotlib:
# This assignment is for visualization using matplotlib:
# data to use:
# url=https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv
# titanic = pd.read_csv(url)
# Charts to plot:
# 1. Create a pie chart presenting the male/female proportion
# 2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender

# In[10]:


data = pd.read_csv('https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv')
data.head(5)


# In[11]:


#a. Create a pie chart presenting the male/female proportion
s=round((data['sex'].value_counts())/len(data)*100,2)
pd.DataFrame(s)


# In[12]:


labels = ['male','female']
sizes = data.sex.value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, colors = ['Green'
,'Red'])
#ax1.axis('equal')
plt.show()


# In[15]:


# b. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender
plt.figure()
category1 = data[data.sex=='male'].plot.scatter('age', 'fare', color='blue',label='male')
data[data.sex=='female'].plot.scatter('age', 'fare',color='red',label='female',ax=category1)


# In[ ]:




