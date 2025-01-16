#impoprt modules
import pandas as pd
import numpy as np
#dataframes
a=pd.read_csv("test.csv")
#print (a)
#null values check
b=a.isnull().sum()

#mean age for filling age column with mean
mean_age=a["Age"].mean()
print ("mean age is",mean_age)
#checking duplicates
print("duplicates numbers are ")
print (a.duplicated().sum())
#filling empty age columns with mean age
a["Age"].fillna(mean_age,inplace=True)
print (a)
#c=a.isnull().sum()
#rint (c)
#filling cabin with unknown
a["Cabin"].fillna("Unknown", inplace=True)
print(a.isnull().sum())
print (a.head(20))

mean_fare=a["Fare"].mean()
#filling fare with mean fare
a["Fare"].fillna(mean_fare,inplace=True)
#print(a)
print (a.isnull().sum())
a['is_correctly_capitalized'] = a['Name'].str.istitle()
print  (a)
print(a.dtypes)


