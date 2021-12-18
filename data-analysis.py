import pandas as pd
import numpy as np

df.shape

df.isnull().sum()

drop_col = df.isnull().sum()[df.isnull().sum()>35/100 * df.shape[0]]
drop_col
drop_col.index

df.drop(drop_col.index ,axis=1 ,inplace=True)
df.isnull().sum()

df.fillna(df.mean(), inplace=True)
df.isnull().sum()

df['Embarked'].describe()

df['Embarked'].fillna('S', inplace= True)

df.isnull().sum()

df.corr()




df.groupby(['Embarked'])['Survived'].mean()
