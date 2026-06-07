#Lab10: Creating Pandas DataFrame From  another DataFrame

import pandas as pd

mydata = {
    'Name': ['Srinivas', 'Vas', 'Hello'],
    'Age': [25, 30, 35],
    'Course': ['ML', 'DevOps', 'Java']
}

df1 = pd.DataFrame(mydata)

print(df1)
print("-"*25)

# df2 = pd.DataFrame(df1) # Shallow Copy

df2=df1           # Shallow Copy
print(df2)
print("-"*25)

df3 = df1.copy()          # Deep Copy
print(df3)

print(id(df1))
print(id(df2))
print(id(df3))

print(df1 is df2)
print(df1 is df3)