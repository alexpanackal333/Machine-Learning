#!/usr/bin/env python
# coding: utf-8

# Problem statement
# Build the linear regression model using scikit learn in boston data to predict
# 'Price' based on other dependent variable.
# 
# 

# In[51]:


from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[25]:


boston_data= load_boston()


# In[26]:


boston=pd.DataFrame(data = boston_data.data, columns=boston_data.feature_names )


# In[28]:


boston.head()


# In[30]:


print(boston_data.DESCR)


# In[90]:


boston=boston.drop(['INDUS','NOX','AGE'],axis=1) #dropping these rows based on OLS summary after 1st iteration


# In[91]:


boston['MEDV']=boston_data.target


# In[92]:


boston.describe()


# In[93]:


sns.relplot(x = 'CRIM', y = 'MEDV', data = boston)


# In[94]:


#boston = sns.load_dataset("boston")
sns.pairplot(boston)


# In[95]:


plt.figure(figsize=(16, 6))
# Store heatmap object in a variable to easily access it when you want to include more features (such as title).
# Set the range of values to be displayed on the colormap from -1 to 1, and set the annotation to True to display the correlation values on the heatmap.
heatmap = sns.heatmap(boston.corr(), vmin=-1, vmax=1, annot=True)
# Give a title to the heatmap. Pad defines the distance of the title from the top of the heatmap.
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12);


# In[96]:


boston.isnull().sum()


# In[97]:


Y=boston['MEDV']
Y


# In[98]:


X=boston.drop(['MEDV'],axis=1)
X


# In[99]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=10)


# In[100]:


print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_train.shape)


# In[101]:


LR=LinearRegression()


# In[102]:


LR.fit(X_train,Y_train)


# In[103]:


LR.coef_


# In[104]:


LR.intercept_


# In[105]:


Y_Pred = LR.predict(X_test)


# In[106]:


Y_Pred


# In[107]:


from sklearn.metrics import r2_score
r2_score(y_pred=Y_Pred, y_true=Y_test)


# In[86]:


import statsmodels.api as sm


# In[87]:


ols= sm.OLS(Y_train,X_train).fit()


# In[88]:


print(ols.summary())


# In[ ]:




