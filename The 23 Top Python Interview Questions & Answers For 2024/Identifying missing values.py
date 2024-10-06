'''Identifying missing values 
We can identify missing values in the DataFrame by using the `isnull()` function and then applying `sum()`. `Isnull()` will return boolean values, and the sum will give you the number of missing values in each column. 

In the example, we have created a dictionary of lists and converted it into a pandas DataFrame. After that, we used isnull().sum() to get the number of missing values in each column.  
'''

import pandas as pd
import numpy as np

# dictionary of lists
dict = {'id':[1, 4, np.nan, 9],
        'Age': [30, 45, np.nan, np.nan],
        'Score':[np.nan, 140, 180, 198]}

# creating a DataFrame
df = pd.DataFrame(dict)

print(df.isnull().sum())
# id       1
# Age      2
# Score    1