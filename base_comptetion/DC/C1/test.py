
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': [0, 0], 'B': [4, 4]})
df2 = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})

df1 = pd.DataFrame({'A': [0, 0], 'B': [None, 4]})
df2 = pd.DataFrame({'A': [1, 1], 'B': [None, 3]})
print(df1)
print(df2)
# df = df1.combine(df2,np.min)
