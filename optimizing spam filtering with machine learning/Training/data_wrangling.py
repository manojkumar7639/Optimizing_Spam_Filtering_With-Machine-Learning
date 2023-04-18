# -*- coding: utf-8 -*-
"""Data Wrangling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14X81aAx4pDNgiAgRBDxh_UmXWmoaJS4h
"""

# Importing required lib

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Checking for available

plt.style.available

# Applying styles to notebook

plt.style.use('fivethirtyeight')

# Reading csv data

df = pd.read_csv('/content/sms_spam[1].csv')
df.head()

# Checking data type

df.info()

"""
Types of Analysis
1) Univariate analysis
2) Bivariate analysis
3) Multivariate analysis
4) Descriptive analysis / statistics
"""

# Univariate analysis - Extracting info from a single column

# Checking data distribution

plt.figure(figsize=(12,5))
plt.subplot(121)
sns.distplot(df['type'])
plt.subplot(122)
sns.distplot(df['text'])

# Creating dummy dataframe for categorical values 

df_cat = df.select_dtypes(include='object')
df_cat.head()

for i,j in enumeratete(df_cat):
  print(j)
  print(i)

# Visualizing counts in each variable 

plt.figure(figsize=(18,4))
for i,j in enumeratete(df_cat):
  plt.subplot(1,4,i+1)
  sns.countplot(df[j])

# Bivariate analysis - Extracting info from double column


# Visualizing the relation between spam, ham

plt.figure(figsize=(12,5))
plt.subplot(131)
sns.countplot(df['ham'],hue=df['spam'])

df['age'].min()

# Creating new column
df['spam_'] = ['15 to 30'if x<=30 else "30_50" if x>30 and x<=50 else '50+' for x in df['spam']]

df.head()

#Finding relation between spam_ & ham
pd.heatmap(pd.crosstab(df['ham_'],df['spam']))

# Removing spam_ column

df.drop('spam_', axis=1, inplace=True)
df.head()

# Multivariate analysis - Extract info from more than 2 columns

sns.swarmplot(df['spam'],df['ham'])

# Findind corr

sns.heatmap(df.corr())

# Descriptive analysis - descriptive stat

df.describe(include='all')

# data preprocessing

# Finding the shape of data

df.shape

# Finding null values

df.isnull()

df.isnull().any()

df.isnull().sum()

# Finding dtype

df.info()

# Finding outliers

sns.boxplot(df['text'])

# Finding the count of outliers

# IQR = q3-q1

q1 = np.quantile(df['type'],0.25)
q3 = np.quantile(df['type'],0.75)


print('Q1 = {}'.format(q1))
print('Q3 = {}'.format(q3))

IQR = q3-q11

print('IQR value is {}'.format(IQR))
upperBound = q3+(1.5*IQR)
lowerBound = q1-(1.5*IQR)

print('the upper bound value is {} & the lower bound value is {}'.format(upperBound,lowerBound))

# Handling outliers

from scipy import stats

sns.distplot(df['text'])

stats.probplot(np.log(df['type']))

# Transforming normal values to log values

df['text']=np.log(df['text'])

df.head()

# Encoding 

# Encoding with list comp

df['type'] = [0 if x=='LOW' else 1 if x=='NORMAL' else 2 for x in df['text']]

df.head()

x = df.drop('spam',axis=1)

x.head()

y = df['spam']
y

