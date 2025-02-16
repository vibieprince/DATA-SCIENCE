import numpy as np
import pandas as pd
ser = pd.Series(np.random.rand(34))
print(ser)
print(type(ser))
newDf = pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
print(newDf)
print(type(newDf))
print(newDf.describe())
print(newDf.dtypes)
newDf[0][0] = "Prince"
print(newDf)
print(newDf.index)
print(newDf.columns)
print(newDf.to_numpy())
newDf[0][0] = 0.3
print(newDf.head())
print(newDf.T) # Transpose
print(newDf.sort_index(axis=1,ascending=False)) #Descending order sort in column
print(newDf[0])
print(type(newDf[0]))
newDf2 = newDf # Not copy but view
newDf2[0][0] =  9273
print(newDf) # Change in newDf because of change in newDf2

# To create copy
# newDf2 = newDf[1]
newDf2 = newDf.copy()

# Now if i change newDf2, there will not be any change in newDf

newDf.loc[0,0] = 654
print(newDf.head(2))
newDf.columns = list("ABCDE")
print(newDf)
newDf.loc[0,0] = 654
print(newDf)
newDf = newDf.drop(0,axis=1)
print(newDf)
print(newDf.loc[[1,2],['C','D']])
print(newDf.loc[[1,2],:])
print(newDf.loc[:,['C','D']])
print(newDf.loc[(newDf['B']<0.3)])
print(newDf.loc[(newDf['A']<0.3) & (newDf['C']>0.1)])
print(newDf.head())
print(newDf.iloc[0,4])
print(newDf.iloc[[0,4],[1,2]])
print(newDf.head(3))
print(newDf.drop(['A'],axis=1))
print(newDf.drop(['A','C'],axis=1))
print(newDf.drop(['A','C'],axis=1,inplace=True)) # For changing originally
print(newDf.reset_index())
print(newDf.reset_index(drop=True,inplace=True))
newDf.loc[:,['B']] = None
print(newDf['B'].isnull())