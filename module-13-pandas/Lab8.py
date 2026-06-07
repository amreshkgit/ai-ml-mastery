#Lab8: Creating Pandas DataFrame From List of Series
import pandas as pd
mydata = [
    pd.Series(['Srinivas', 20, 'Machine Learning']),
    pd.Series(['Vas', 25, 'Java Fullstack']),
    pd.Series(['Hello', 30, 'Deep Learning']),
    pd.Series(['Dande', 23, 'Machine Learning']),
]

df = pd.DataFrame(mydata)
print(df)

print("-"*25)

df.columns = ['Name', 'Age', 'Course']  # Set column names
print(df)