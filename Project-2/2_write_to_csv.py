import pandas as pd
df= pd.read_csv('Project-2/customers-100.csv')
df.to_csv('new_csv.csv', index = False)
