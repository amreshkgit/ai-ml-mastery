# Lab6: Reading from JSON file

import pandas as pd

df = pd.read_json("myjlc.json")
print(type(df))