import pandas as pd
import numpy as np

#creating empty series
ser = pd.Series()
print(ser)

#creating simple array
arr = np.array(['a','b','c','d','e','f'])
print("This is array : ",arr)

ser = pd.Series(arr)
print(ser)