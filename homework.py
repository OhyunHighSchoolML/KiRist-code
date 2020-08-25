import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

df2 = pd.read_excel('/content/mountain.xlsx')

df2.loc['sum'] = None
df2.iloc[60,0] = "2020/08/24"
df2['sum_month'] = None
df2.iloc[60,1] = df2['어리목'].sum()
df2.iloc[60,2] = df2['영실'].sum()
df2.iloc[60,3] = df2['성판악'].sum()
df2.iloc[60,4] = df2['관음사'].sum()
df2.iloc[60,5] = df2['돈내코'].sum()
for i in range(len(df2)):
  df2['sum_month'].iloc[i] = df2.drop('구분',axis=1).iloc[i].sum()
 df2
