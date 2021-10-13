import numpy as np
import pandas as pd

df1 = pd.read_csv('test10.csv')
df2 = pd.read_csv('test9.csv')

print(df1.equals(df2))

print(df1.keys)
print(df2.keys)