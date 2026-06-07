# Lab2: Creating Pandas  Series
import pandas as pd
myseries2 = pd.Series(data=[100, 200, 300, 400, 500],index=['a', 'b', 'c','d','e'])
print(myseries2)
print("-"*25)
print(myseries2['a'])
print(myseries2['b'])
x = myseries2["c"]
print(x)
print(type(x))
