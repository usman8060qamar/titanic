#import modules
import pandas as pd
import numpy as np
#loading data 
df=pd.read_csv("train.csv")
#print (df)
print (df.isnull().sum())
mean_age=df["Age"].mean()
df["Age"].fillna(mean_age,inplace=True)
print (df.isnull().sum())
df["Cabin"].fillna("Unknown cabin",inplace=True)
df["Embarked"].fillna(method="ffill",inplace=True)
print(df.isnull().sum())
print (df)