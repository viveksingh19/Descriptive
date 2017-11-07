
# coding: utf-8

# In[10]:

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().system('pip install seaborn')
import seaborn as sns
data = pd.read_csv('D:/Python/DATA/pokemon.csv')

print(data)
data.info()


# In[15]:

#Correlation map

f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)


# In[17]:

data.head(10)


# In[19]:

data.columns


# In[21]:

# Descriptive Plots

# Line Plot
# color = color, label = label, linewidth = width of line, alpha = opacity, grid = grid, linestyle = sytle of line
data.Speed.plot(kind = 'line', color = 'g',label = 'Attack',linewidth=1,alpha = 0.5,grid = True,linestyle = ':')
data.Defense.plot(color = 'r',label = 'Defense',linewidth=1, alpha = 0.5,grid = True,linestyle = '-.')
plt.legend(loc='upper right')     # legend = puts label into plot
plt.xlabel('x axis')              # label = name of label
plt.ylabel('y axis')
plt.title('Line Plot')            # title = title of plot



# In[23]:

# Scatter Plot 
# x = attack, y = defense
data.plot(kind='scatter', x='Attack', y='Defense',alpha = 0.5,color = 'red')
plt.xlabel('Attack')              # label = name of label
plt.ylabel('Defence')
plt.title('Attack Defense Scatter Plot')            # title = title of plot


# In[26]:

data.Speed.plot(kind = 'hist',bins = 50,figsize = (15,15))

