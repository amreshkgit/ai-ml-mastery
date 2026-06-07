#Lab9: Creating Pandas DataFrame From  List of Lists

import pandas as pd
mydata = [
 ['Srinivas', 20, 'Machine Learning'],
 ['Vas', 25, 'Java Fullstack'],
 ['Hello', 30, 'Deep Learning']
]
df1 = pd.DataFrame(mydata)
print(df1)
print("-"*25)
df2 = pd.DataFrame(data=mydata, columns=['Name', 'Age', 'Course'])
print(df2)