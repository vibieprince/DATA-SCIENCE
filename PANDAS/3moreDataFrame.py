import pandas as pd
import numpy as np
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})
print(df.dropna())
print(df.head())
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, np.nan, np.nan],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})
print(df.dropna(how='all',axis=1))
print(df.head())
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Alfred'],
                   "toy": [np.nan, np.nan, np.nan],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})
print(df.drop_duplicates())
print(df.drop_duplicates(subset=['name'],keep=False)) # Keep='first'/'last'
print(df.shape)
print(df.info)
print(df['name'].value_counts(dropna=False))
data = pd.read_excel('data.xlsx')
print(data)
data = pd.read_excel('data.xlsx',sheet_name='Sheet2')
print(data)
data.to_excel('data.xlsx',sheet_name='Sheet2') # But this will remove the sheet1
# So to overcome this 
data1 = data.copy()
with pd.ExcelWriter('data.xlsx') as writer:
    data.to_excel(writer,sheet_name='Sheet1')
    data1.to_excel(writer,sheet_name='Sheet2')