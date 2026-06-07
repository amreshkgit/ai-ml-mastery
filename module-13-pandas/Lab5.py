# Lab5: Reading from Excel file
import pandas as pd

df = pd.read_excel("myjlc.xlsx")
print(type(df))

print(df)