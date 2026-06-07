#Lab7: Creating Pandas DataFrame From Dictionary
import pandas as pd

mydata = {
    'Name': ['Srinivas', 'Vas', 'Hello'],
    'Age': [25, 30, 35],
    'Course': ['Machine Learning', 'Java Fullstack', 'Deep Learning']
}

df = pd.DataFrame(mydata)
print(df)
