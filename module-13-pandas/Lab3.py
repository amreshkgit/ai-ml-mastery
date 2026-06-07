#Lab3: Creating Pandas DataFrame:
# From a dictionary
import pandas as pd
mydata={
    'Name': ['Hello', 'Sri', 'Vas'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(mydata)
print(type(df))